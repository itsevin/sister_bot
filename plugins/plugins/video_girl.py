from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    PrivateMessageEvent,
    MessageSegment
)
import httpx


xjjsp = on_command(
    '小姐姐视频',
    block=True,
    priority=11
)


@xjjsp.handle()
async def main(event: GroupMessageEvent):
    await xjjsp.finish("此功能仅限于私聊，请加好友使用")


@xjjsp.handle()
async def main(event: PrivateMessageEvent):
    msg = await get_data()
    await xjjsp.finish(MessageSegment.video(msg))


async def get_data():
    url = 'https://tucdn.wpon.cn/api-girl/index.php?wpon=url'
    async with httpx.AsyncClient(verify=False) as client:
        resp = await client.get(url)
        data = "https:" + resp.text.strip()
    return data
