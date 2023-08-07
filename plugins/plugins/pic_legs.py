from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    PrivateMessageEvent,
    MessageSegment
)
import httpx


kt = on_command(
    '看腿',
    block=True,
    priority=11
)


@kt.handle()
async def main(event: GroupMessageEvent):
    await kt.finish("此功能仅限于私聊，请加好友使用")


@kt.handle()
async def main(event: PrivateMessageEvent):
    msg = await get_pic()
    await kt.finish(MessageSegment.image(msg))


async def get_pic():
    url = 'http://81.70.100.130/api/tu.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("\n", "").strip()
    return data
