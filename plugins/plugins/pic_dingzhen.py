from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx


dingzhen = on_command(
    '丁真',
    block=True,
    priority=11
)


@dingzhen.handle()
async def main():
    msg = await get_data()
    await dingzhen.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://api.sevin.cn/api/dingzhen.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.strip()
    return data
