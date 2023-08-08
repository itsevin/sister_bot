import asyncio
import os
import platform
import shutil
import tarfile
import httpx
import subprocess
import ujson as json
from pathlib import Path
from typing import Tuple

from nonebot import logger, get_driver
from nonebot.adapters.onebot.v11 import Bot, Message
from utils.config import Config


driver = get_driver()

release_url = "https://api.github.com/repos/itsevin/sister_bot/releases"

_version_file = Path() / "__version__"
update_tar_file = Path() / "update_tar_file.tar.gz"
temp_dir = Path() / "temp"
backup_dir = Path() / "backup"

proxy = Config.get_value("proxy", "proxy")
if proxy:
    proxies = {
        "http://": proxy,
        "https://": proxy
    }
else:
    proxies = None


class NoVersionData(Exception):
    pass


class NoVersionMatch(Exception):
    pass


@driver.on_bot_connect
async def remind(bot: Bot):
    if str(platform.system()).lower() == "windows":
        restart = Path() / "restart.bat"
        if not restart.exists():
            port = str(bot.config.port)
            script = f'''
@echo off
set PORT={port}

for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":%PORT%"') do (
taskkill /PID %%a /F
goto :RunPoetry
)

:RunPoetry
call poetry run nb run
'''
            with open(restart, "w", encoding="utf-8") as f:
                f.write(script)
            logger.info("已自动生成 restart.bat(重启) 文件，请检查脚本是否与本地指令符合")
    else:
        restart = Path() / "restart.sh"
        if not restart.exists():
            port = str(bot.config.port)
            script = f'''
pid=$(netstat -tunlp | grep {port} | awk '{{print $7}}')
pid=${{pid%/*}}
kill -9 $pid
sleep 3
poetry run nb run
'''
            with open(restart, "w", encoding="utf-8") as f:
                f.write(script)
            os.system("chmod +x ./restart.sh")
            logger.info("已自动生成 restart.sh(重启) 文件，请检查脚本是否与本地指令符合")
    is_restart_file = Path() / "is_restart"
    if is_restart_file.exists():
        with open(is_restart_file, "r", encoding="utf-8") as f:
            user_id=f.read()
        if user_id:
            await bot.send_private_msg(
                user_id=int(user_id),
                message="机器人重启完毕",
            )
        is_restart_file.unlink()


async def check_update(bot: Bot) -> Tuple[int, str]:
    logger.info("开始检查更新机器人")
    _version = "v0.0.0"
    if _version_file.exists():
        with open(_version_file, "r", encoding="utf-8") as f:
            _version = f.readline().split(":")[-1].strip()
    else:
        raise NoVersionData(f"找不到机器人版本信息文件，无法检测更新，版本信息文件应该位于{_version_file}")
    status_get_version_data, data = await get_version_data()
    if not status_get_version_data:
        return 995, data
    global releases_version
    releases_version = "v0.0.0"
    if data:
        if data[0]["name"] != _version:
            latest_version = data[0]["name"]
            version_match = False
            for releases in data:
                if _version == releases["name"]:
                    version_match = True
                    break
                if not releases["prerelease"] or Config.get_value("releases", "releases") == "dev":
                    releases_version = releases["name"]
                    tar_gz_url = releases["tarball_url"]
                    update_info = releases["body"]
                    time = releases['created_at']
            if version_match != True:
                raise NoVersionMatch(f"找不到与远程仓库版本相匹配的机器人版本信息文件中的版本，无法检测更新，版本信息文件应该位于{_version_file}")
            logger.info(f"检测到机器人需要更新，当前版本：{_version}，下一版本：{releases_version}，最新版本：{latest_version}")
            for superuser in list(bot.config.superusers):
                await bot.send_private_msg(
                    user_id=int(superuser),
                    message=f"检测到机器人需要更新，当前版本：{_version}，下一版本：{releases_version}，最新版本：{latest_version}\n" f"开始更新",
                )
            logger.debug(f"开始下载机器人 {releases_version} 版本文件")
            async with httpx.AsyncClient(proxies=proxies) as client:
                resp = await client.get(tar_gz_url)
                tar_gz_url = resp.headers.get("Location")
            async with httpx.AsyncClient(proxies=proxies) as client:
                resp = await client.get(tar_gz_url)
                status_code = resp.status_code
                file_data = resp.content
            if status_code == 200:
                with open(update_tar_file, "wb") as f:
                    f.write(file_data)
                logger.debug("下载机器人新版文件完成")
                error_info = await asyncio.get_event_loop().run_in_executor(
                    None, _update_handle
                )
                if error_info:
                    return 996, error_info
                logger.info("机器人更新完毕，清理文件完成")
                global nb_config_desc
                global update_desc
                msg = (
                            f"机器人更新完成，版本：{_version} -> {releases_version}\n"
                            f"版本发布日期：{time}\n"
                            f"更新日志：\n"
                            f"{update_info}"
                        )
                if nb_config_desc:
                    msg += f"\nnonebot配置更新说明：\n{nb_config_desc}"
                if update_desc:
                    msg += f"\n更新说明：\n{update_desc}"
                for superuser in list(bot.config.superusers):
                    await bot.send_private_msg(
                        user_id=int(superuser),
                        message=msg
                    )
                return 200, ""
            else:
                error_info = f"下载机器人最新版本失败，版本号：{releases_version}"
                return 997, error_info
        else:
            error_info = f"自动获取机器人版本成功：{_version}，当前版本为最新版，无需更新"
            return 999, error_info
    else:
        error_info = "自动获取机器人版本信息请求成功，但是未获取到有效信息"
        return 998, error_info


def _update_handle() -> str:
    if not temp_dir.exists():
        temp_dir.mkdir(exist_ok=True, parents=True)
    if backup_dir.exists():
        shutil.rmtree(backup_dir)
    tar_file = None
    backup_dir.mkdir(exist_ok=True, parents=True)
    logger.info("开始解压机器人文件压缩包....")
    tar_file = tarfile.open(update_tar_file)
    tar_file.extractall(temp_dir)
    logger.info("解压机器人文件压缩包完成....")
    bot_new_file = Path(temp_dir) / os.listdir(temp_dir)[0]
    update_info_file = Path(bot_new_file) / "update_info.json"
    with open(update_info_file, "r", encoding="utf-8") as f:
        update_info = json.load(f)
    
    global nb_config_desc
    global update_desc
    update_file = update_info["file"]["update_file"]
    add_file = update_info["file"]["add_file"]
    delete_file = update_info["file"]["delete_file"]
    move_file = update_info["file"]["move_file"]
    add_bot_config = update_info["config"]["bot"]["add_bot_config"]
    delete_bot_config = update_info["config"]["bot"]["delete_bot_config"]
    move_bot_config = update_info["config"]["bot"]["move_bot_config"]
    nb_config_desc = update_info["config"]["nonebot"]["nb_config_desc"]
    update_desc = update_info["desc"]["update_desc"]
    
    if add_bot_config:
        for c in add_bot_config:
            Config.add_plugin_config(
                module=c["module"],
                key=c["key"],
                value=c["value"],
                help_=c["help"],
                default_value=c["default_value"],
                type_=c["type"]
            )
    if delete_bot_config:
        for c in delete_bot_config:
            Config.delete_plugin_config(
                module=c["module"],
                key=c["key"]
            )
    if move_bot_config:
        for i in move_bot_config:
            c = Config.get_config(
                module=i["old"]["module"],
                key=i["old"]["key"]
            )
            if c:
                Config.add_plugin_config(
                    module=c["new"]["module"],
                    key=c["new"]["key"],
                    value=c.value,
                    help_=c.help_,
                    default_value=c.default_value,
                    type_=c.type_
                )
                Config.delete_plugin_config(
                    module=c["old"]["module"],
                    key=c["old"]["key"]
                )
    logger.debug("配置已更新")

    for f in delete_file + update_file:
        file_path = Path() / f
        backup_file_path = Path(backup_dir) / f
        if file_path.exists():
            backup_file_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(file_path.absolute(), backup_file_path.absolute())
            if f in delete_file:
                logger.debug(f"已删除并备份文件： {f}")
    for f in add_file + update_file:
        new_file_path = Path(bot_new_file) / f
        old_file_path = Path() / f
        if old_file_path.exists() and f in add_file:
            backup_file_path = Path(backup_dir) / f
            shutil.move(old_file_path.absolute(), backup_file_path.absolute())
            logger.warning(f"文件 {f} 为更新信息中的添加文件，但是该文件已存在，已自动更新该文件为新版本并完成备份")
        elif new_file_path.exists():
            shutil.move(new_file_path.absolute(), old_file_path.absolute())
            if f in add_file:
                logger.debug(f"已更新文件： {f}")
            elif f in update_file:
                logger.debug(f"已更新并备份文件： {f}")
        elif not new_file_path.exists():
            logger.error(f"尝试从新版本文件中更新文件 {f} ，但是新版本文件中不存在该文件")
    for f in move_file:
        new_file_path = Path() / f["new"]
        old_file_path = Path() / f["old"]
        old_file = f["old"]
        new_file = f["new"]
        if new_file_path.exists():
            new_file_path.parent.mkdir(exist_ok=True, parents=True)
            shutil.move(old_file_path.absolute(), new_file_path.absolute())
            logger.debug(f"已移动文件 {old_file} 至 {new_file}")
        else:
            logger.warning(f"尝试移动文件 {old_file} 至 {new_file} ，但是原文件不存在，跳过处理")

    if tar_file:
        tar_file.close()
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    if update_tar_file.exists():
        update_tar_file.unlink()
    local_update_info_file = Path() / "update_info.json"
    if local_update_info_file.exists():
        local_update_info_file.unlink()
    global releases_version
    with open(_version_file, "w", encoding="utf-8") as f:
        f.write(f"__version__: {releases_version}")

    for i in range(1, 4):
        try:
            subprocess.run(['poetry', 'install'], check=True, cwd=Path())
            return ""
        except subprocess.CalledProcessError as e:
            error_message = str(e)
            if i == 3:
                error_info = f"更新依赖项失败，请自行排查问题并在机器人目录终端手动尝试更新，更新命令 'poetry install' ，错误信息：{error_message}"
                return error_info


# 获取版本信息
async def get_version_data() -> tuple[bool, any]:
    for i in range(3):
        try:
            async with httpx.AsyncClient(timeout=30, proxies=proxies) as client:
                resp = await client.get(release_url)
                if resp.status_code == 200:
                    return True, json.loads(resp.text)
        except httpx.ReadTimeout:
            if i == 2:
                error_info = "检查更新机器人获取远程仓库版本超时，请检查网络环境"
                return False, error_info
        except Exception as e:
            if i == 2:
                error_info = f"检查更新机器人获取远程仓库版本失败 {type(e)}：{e}"
                return False, error_info
