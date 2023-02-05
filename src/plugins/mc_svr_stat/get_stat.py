import nonebot
from mcstatus import BedrockServer, JavaServer
from nonebot.adapters.onebot.v11 import MessageSegment


def del_escape(string: str):
    # 48-57(0-9),65-90(A-Z),97-122(a-z)
    for i in range(48, 57 + 1):
        string = string.replace(f"§{chr(i)}", "")
    for i in range(65, 90 + 1):
        string = string.replace(f"§{chr(i)}", "")
    for i in range(97, 122 + 1):
        string = string.replace(f"§{chr(i)}", "")
    return string


async def motd(address: str, full=False):
    address = address.strip().replace("：", ":")
    if not address:
        if full:
            return MessageSegment.text(
                "[MCJE服务器信息]\n"
                "正确用法:\n"
                "!motdfull <服务器IP> (电脑版)\n"
                "!motdpe <服务器IP> (手机版)"
            )
        else:
            return MessageSegment.text(
                "[MCJE服务器信息]\n"
                "正确用法:\n"
                "!motd <服务器IP> (电脑版)\n"
                "!motdpe <服务器IP> (手机版)"
            )
    if address.rfind(":") == -1:
        address += ":25565"

    try:
        ret = JavaServer.lookup(address)
        ret = await ret.async_status()
        latency = ret.latency
        desc = ret.description
        ret_raw = ret.raw
    except Exception as e:
        nonebot.logger.opt(colors=True, exception=e).error("")
        return MessageSegment.text(f"[MCJE服务器信息]\n操作失败：{e!r}")

    pic_text = ""
    if ret.favicon:
        pic_b64: str = ret.favicon
        pos = pic_b64.find("base64,")
        if pos != -1:
            pic_b64 = pic_b64[pos + 7 :]
        pic_text = "显示图标：" + MessageSegment.image(f"base64://{pic_b64}") + "\n"

    players = ""
    if ret.players.sample:
        player_list = [del_escape(x.name) for x in ret.players.sample]
        player_list = [x for x in player_list if x]
        if full:
            players = f'玩家列表：{", ".join(player_list)}\n'
        else:
            players = f'玩家列表（最多显示十个）：{", ".join(player_list[:10])}\n'

    mod_info = ""
    if "modinfo" in ret_raw:
        if ret_raw["modinfo"]["modList"]:
            mod_list = "\n".join(
                [f'{x["modid"]} - {x["version"]}' for x in ret["modinfo"]["modList"]][
                    :10
                ]
            )
            if full:
                mod_info = f"Mod列表：{mod_list[:10]}"
            else:
                mod_info = f"Mod列表（最多显示十个）：{mod_list[:10]}"
        else:
            mod_info = "Mod列表：无"
        mod_info = f'\nMod端类型：{ret["modinfo"]["type"]}\n{mod_info}'

    players_online = ret.players.online
    players_max = ret.players.max
    online_percent = round(players_online / players_max * 100, 2)

    full_tip = "" if full else f"\n注：使用 !motdfull 查看全部玩家列表及mod列表"

    return (
        MessageSegment.text(f"[MCJE服务器信息]\n")
        + pic_text
        + MessageSegment.text(
            f"服务端名：{ret.version.name}\n"
            f"协议版本：{ret.version.protocol}\n"
            f"当前人数：{players_online}/{players_max}({online_percent}%)\n"
            f"{players}"
            f"描述文本：\n{del_escape(desc)}\n"
            f"游戏延迟：{latency:.2f}ms"
            f"{mod_info}"
            f"{full_tip}"
        )
    )


async def motdpe(address: str):
    address = address.strip().replace("：", ":")
    if not address:
        return MessageSegment.text(
            "[MCBE服务器信息]\n" "正确用法:\n" "!motd <服务器IP> (电脑版)\n" "!motdpe <服务器IP> (手机版)"
        )
    if address.rfind(":") == -1:
        address += ":19132"

    try:
        ret = BedrockServer.lookup(address)
        ret = await ret.async_status()
    except Exception as e:
        nonebot.logger.opt(colors=True, exception=e).error("")
        return MessageSegment.text(f"[MCBE服务器信息]\n操作失败：{e!r}")

    map_name = f"存档名称：{del_escape(ret.map)}\n" if ret.map else ""
    game_mode = f"游戏模式：{ret.gamemode}\n" if ret.gamemode else ""
    online_percent = round(int(ret.players_online) / int(ret.players_max) * 100, 2)

    return MessageSegment.text(
        "[MCBE服务器信息]\n"
        f"协议版本：{ret.version.protocol}\n"
        f"游戏版本：{ret.version.version}\n"
        f"描述文本：{del_escape(ret.motd)}\n"
        f"在线人数：{ret.players_online}/{ret.players_max}({online_percent}%)\n"
        f"{map_name}"
        f"{game_mode}"
        f"游戏延迟：{ret.latency * 1000:.2f}ms"
    )
