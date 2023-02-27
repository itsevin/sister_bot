import json
from datetime import datetime
from functools import wraps

import aiohttp
from nonebot import logger, on_command
from nonebot.adapters.onebot.v11 import ActionFailed, MessageEvent
from nonebot.adapters.onebot.v11.message import Message, MessageSegment
from nonebot.exception import FinishedException
from nonebot.matcher import Matcher
from nonebot.params import CommandArg


def default_parser(args):
    return args.extract_plain_text()


def error_handle():
    def wrapper(func):
        @wraps(func)
        async def decorator(**kwargs):
            try:
                return await func(**kwargs)
            except (ActionFailed, FinishedException):
                raise
            except:
                logger.exception("接口访问出错")
                if matcher := kwargs.get("matcher"):
                    await matcher.finish("接口访问出错，请检查后台输出")

        return decorator

    return wrapper


def format_return(ret, func=None):
    if not func:
        func = lambda x: x

    msg = f'\n[{(code := ret["code"])}]{ret["msg"]}'
    if str(code) == "200":
        msg += "\n--------\n" + func(ret["data"])  # MessageSegment拼接
    return msg + "\n--------\nAPI from https://api.gmit.vip"


async def get_api_resp(name, params, original=False) -> dict | list | bytes:
    async with aiohttp.ClientSession() as s:
        async with s.get(f"https://api.gmit.vip/Api/{name}", params=params) as resp:
            ret = await resp.read()
            return ret if original else json.loads(ret)


def format_json_time(t):
    return (
        datetime.fromisoformat(t.replace("Z", "+00:00"))
        .astimezone()
        .strftime("%Y-%m-%d %H:%M:%S (%Z)")
    )


@on_command("二维码解析", aliases={"解析二维码", "二维码识别", "识别二维码"}).handle()
@error_handle()
async def _(matcher: Matcher, event: MessageEvent, args: Message = CommandArg()):
    if img := args["image"]:
        pass
    elif event.reply and (img := event.reply.message["image"]):
        pass
    else:
        await matcher.finish("请附带/回复要解析的二维码图片")

    await matcher.finish(
        format_return(
            await get_api_resp("QrReader", {"url": img[0].data["url"]}),
            lambda ret: f'识别结果：{ret["text"]}',
        ),
        at_sender=True,
    )


@on_command("二维码生成", aliases={"生成二维码"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入要用于生成二维码的内容")

    await matcher.finish(
        format_return(
            {
                "code": "200",
                "msg": "请求成功",
                "data": MessageSegment.image(
                    await get_api_resp("QrCode", {"text": arg}, original=True)
                ),
            },
            lambda ret: ret,
        ),
        at_sender=True,
    )


@on_command("ping", aliases={"Ping", "PING"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入IP/域名")

    await matcher.finish(
        format_return(
            await get_api_resp("Ping", {"ip": arg}),
            lambda ret: (
                f'查询目标：{ret["host"]}\n'
                f'IP地址：{ret["ip"]}\n'
                f'最小/平均/最大延迟：{ret["ping_min"]}/{ret["ping_avg"]}/{ret["ping_max"]}\n'
                f'主机位置：{ret["location"]}\n'
                f'PING节点：{ret["node"]}'
            ),
        ),
        at_sender=True,
    )


@on_command("ICP查询", aliases={"icp查询", "Icp查询", "备案查询"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("ICP", {"domain": arg}),
            lambda ret: (
                f'查询域名：{ret["domain"]}\n'
                f'网站名称：{ret["serviceName"]}\n'
                f'主页地址：{ret["homeUrl"]}\n'
                f'主办单位名称：{ret["unitName"]}\n'
                f'主办单位性质：{ret["class"]}\n'
                f'备案号：{ret["icp"]}\n'
                f'审核时间：{ret["time"]}'
            ),
        ),
        at_sender=True,
    )


@on_command("拦截检测").handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入网址")

    params = {"url": arg}
    qq = await get_api_resp("TencentUrl", params)
    if qq["code"] != 200:
        await matcher.finish(format_return(qq))

    wx = await get_api_resp("WxUrl", params)
    if wx["code"] != 200:
        await matcher.finish(format_return(wx))

    wx["data"]["qq"] = qq["data"]["type"]
    await matcher.finish(
        format_return(
            wx,
            lambda ret: f'查询网址：{ret["url"]}\nQQ/微信拦截状态：{ret["type"]}/{ret["qq"]}',
        ),
        at_sender=True,
    )


@on_command("收录查询").handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("CheckSEO", {"domain": arg}),
            lambda ret: (
                f'查询域名：{ret["domain"]}\n'
                f'网站标题：{title if (title := ret["title"]) else "未知"}\n'
                f'百度收录量：{ret["baidu"]}\n'
                f'好搜收录量：{ret["haoso"]}\n'
                f'神马收录量：{ret["sm"]}\n'
                f'搜狗收录量：{ret["sogou"]}\n'
                f'Bing/必应中国：{ret["bing"]}/{ret["bingZh"]}\n'
                f'Google：{ret["google"]}'
            ),
        ),
        at_sender=True,
    )


@on_command("sping", aliases={"Sping", "SPing", "SPING"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    arg = arg.split(" ", 1)
    ip = arg[0]
    node_num = 10
    if len(arg) > 1:
        if arg[1].isdigit() and (nn := int(arg[1])) > 0:
            node_num = nn
        else:
            await matcher.finish("请输入有效的节点数量")

    await matcher.finish(
        format_return(
            await get_api_resp("SPing", {"ip": ip, "num": node_num}),
            lambda ret: "\n".join(
                ["节点名 | IP | 平均延迟 | TTL"]
                + [
                    f'{x["node"]} | {x["ip"]} | {f"{avg}ms" if (avg := x["ping_avg"]).isdigit() else avg} | {x["ttl"]}'
                    for x in ret
                ]
            ),
        ),
        at_sender=True,
    )


@on_command("whois查询", aliases={"Whois查询", "WhoIs查询", "WHOIS查询"}).handle()
@error_handle()
async def _(matcher: Matcher, args: Message = CommandArg()):
    if not (arg := args.extract_plain_text()):
        await matcher.finish("请输入域名")

    await matcher.finish(
        format_return(
            await get_api_resp("Whois", {"domain": arg}),
            lambda ret: (
                f'查询域名：{ret["domain"]}\n'
                f'注册商：{ret["registrant"]}\n'
                f'注册邮箱：{ret["email"]}\n'
                f'注册时间：{format_json_time(ret["registrationTime"])}\n'
                f'到期时间：{format_json_time(ret["expirationTime"])}\n'
                f'DNS服务器：{", ".join(ret["nameServer"])}\n'
                f'域名状态：{", ".join([x["info"] for x in ret["domainState"]])}'
            ),
        ),
        at_sender=True,
    )
