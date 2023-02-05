from typing import Any

from nonebot import logger, on_command, on_regex
from nonebot.adapters.onebot.v11 import MessageEvent
from nonebot.internal.params import ArgPlainText
from nonebot.matcher import Matcher
from nonebot.params import CommandArg, RegexGroup
from nonebot.typing import T_State

from .config import config
from .data_source import *

matcher_command = on_command("梗百科")
matcher_regex = on_regex("([\s\S]+)是什么梗")


@matcher_regex.handle()
async def _(matcher: Matcher, state: T_State, args: tuple[Any, ...] = RegexGroup()):
    arg = args[0].strip()
    await get_geng(matcher, arg, state)


@matcher_command.handle()
async def _(state: T_State, event: MessageEvent, args: Message = CommandArg()):
    if event.reply and (reply := event.reply.message).extract_plain_text().strip():
        state["phrase"] = reply
    elif args.extract_plain_text().strip():
        state["phrase"] = args


@matcher_command.got("phrase", "请问你想要了解一下什么梗呢？")
async def _(m: Matcher, state: T_State, phrase: str = ArgPlainText("phrase")):
    if not (phrase := phrase.strip()):
        await m.reject("这条消息没有文本，无法查询……你到底想了解什么梗呢？请再发一遍")

    await get_geng(m, phrase, state)


@matcher_command.handle()
@matcher_regex.handle()
async def _(m: Matcher, state: T_State, event: MessageEvent):
    msg = event.get_plaintext()
    more = state.get("more", {})
    if item := more.get(msg):
        await m.reject(
            "\n" + (await format_definition(item)) + "\n\nTip：继续发送候选项可以接着查询~",
            at_sender=True,
        )
    await m.finish()


def get_numbered_name(names, name):
    count = 0
    numbered_name = name
    while numbered_name in names:
        count += 1
        numbered_name = f"{name}{count}"
    return numbered_name


async def get_geng(m: Matcher, phrase: str, state: T_State):
    try:
        ret = await get_geng_ret(phrase)
    except:
        logger.exception("获取梗失败")
        await m.finish("抱歉，我还没Get到这个梗……（请求接口失败/返回值解析失败）")
    else:
        if not ret.data:
            await m.finish(
                f"抱歉，我还没Get到这个梗……（{ret.message.title}：{ret.message.content}）"
            )

        if definitions := filter_definitions(ret):
            await m.send(
                "\n" + (await format_definition(definitions[0])), at_sender=True
            )
            if len(definitions) > 1 and config.send_suggestion:
                cut = definitions[1 : config.suggestion_num + 1]  # 排除第一个
                more = {get_numbered_name(more.keys(), i.term.title): i for i in cut}
                state["more"] = more

                await m.send(
                    (
                        (("你是否还想找这些：\n" + "\n".join(f"【{x}】" for x in more)) + "\n")
                        + "发送对应梗名字即可继续查询，想重新查询请先发送一条其他消息再发送查询指令~"
                    )
                )

                await m.pause()
        else:
            await m.finish("抱歉，我还没Get到这个梗……（未找到词条）")
