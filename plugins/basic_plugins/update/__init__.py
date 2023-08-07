import os
import platform
import subprocess

from pathlib import Path

from nonebot import on_command, logger, require, get_bot
from nonebot.adapters.onebot.v11 import Bot, Event
from nonebot.params import ArgStr
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

from utils.config import Config

from .source import check_update


update_check = on_command(
    "检查更新", 
    permission=SUPERUSER, 
    rule=to_me(),
    priority=1, 
    block=True
)

restart = on_command(
    "重启",
    permission=SUPERUSER,
    rule=to_me(),
    priority=1,
    block=True,
)


@update_check.handle()
async def _(bot: Bot, event: Event):
    try:
        status_update, error_info = await check_update(bot)
    except Exception as e:
        logger.error(f"检查并更新机器人错误 {type(e)}: {e}")
        await update_check.finish(f"检查并更新机器人错误 {type(e)}: {e}")
    else:
        if status_update == 200:
            if Config.get_value("bot_update", "auto_restart"):
                logger.info("更新完毕，开始重启机器人")
                await restart.send("更新完毕，开始自动重启机器人")
                await bot_restart(event)
            else:
                logger.info("更新完毕，等待重启")
                await update_check.send("更新完毕，请重启机器人\n重启命令： 重启")
        elif status_update == 999:
            logger.info(error_info)
            await update_check.finish(error_info)
        elif status_update:
            logger.error(f"检查并更新机器人错误，错误信息： {error_info}")
            await update_check.finish(f"检查并更新机器人错误\n错误信息：\n{error_info}")


@restart.got("flag", prompt=f"确定是否重启机器人？确定请回复[是|好|确定]（重启失败咱们将失去联系，请谨慎！）")
async def _(event: Event, flag: str = ArgStr("flag")):
    if flag.lower() in ["true", "是", "好", "确定", "确定是"]:
        await restart.send("开始重启机器人..请稍等...")
        await bot_restart(event)
    else:
        await restart.send("已取消操作...")


@scheduler.scheduled_job(
    "cron",
    hour=12,
    minute=0,
)
async def _():
    if Config.get_value("bot_update", "auto_update"):
        bot = get_bot()
        try:
            status_update, error_info = await check_update(bot)
        except Exception as e:
            logger.error(f"检查并更新机器人错误 {type(e)}: {e}")
            for superuser in list(bot.config.superusers):
                await bot.send_private_msg(
                    user_id=int(superuser),
                    message=f"检查并更新机器人错误 {type(e)}: {e}"
                )
        else:
            if status_update == 200:
                if Config.get_value("bot_update", "auto_restart"):
                    logger.info("更新完毕，开始重启机器人")
                    for superuser in list(bot.config.superusers):
                        await bot.send_private_msg(
                            user_id=int(superuser),
                            message="更新完毕，开始自动重启机器人"
                        )
                    await bot_restart()
                else:
                    logger.info("更新完毕，等待重启")
                    for superuser in list(bot.config.superusers):
                        await bot.send_private_msg(
                            user_id=int(superuser),
                            message="更新完毕，请重启机器人\n重启命令： 重启"
                        )
            elif status_update == 999:
                logger.info(error_info)
            elif status_update:
                logger.error(f"检查并更新机器人错误，错误信息： {error_info}")
                for superuser in list(bot.config.superusers):
                    await bot.send_private_msg(
                        user_id=int(superuser),
                        message=f"检查并更新机器人错误\n错误信息：\n{error_info}"
                    )


async def bot_restart(event=None):
    with open("is_restart", "w", encoding="utf-8") as f:
        if event:
            f.write(event.get_session_id())
    if str(platform.system()).lower() == "windows":
        subprocess.run(["restart.bat"], cwd=Path())
    else:
        subprocess.run(["./restart.sh"], cwd=Path())
