import random

import aiofiles
from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Event, MessageSegment, PokeNotifyEvent
from nonebot.matcher import Matcher
from nonebot.rule import to_me

from .config import config as conf


async def read_file(file_name):
    async with aiofiles.open(file_name, "rb") as f:
        ret = await f.read()
    return ret


async def get_msg():
    reply = random.choice(conf)
    msg = None
    if reply.type == "image":
        msg = MessageSegment.image(await read_file(reply.content))
    elif reply.type == "text":
        msg = reply.content
    return msg, reply.action


@on_notice(rule=to_me()).handle()
async def _(event: Event, matcher: Matcher, _: PokeNotifyEvent):
    reply, action = await get_msg()
    if reply:
        await matcher.send(reply)
        if action:
            await matcher.send(MessageSegment("poke", {"qq": event.user_id}))
