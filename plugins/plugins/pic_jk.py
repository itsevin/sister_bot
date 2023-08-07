from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx


jk = on_command(
    'jk',
    block=True,
    priority=11
)


@jk.handle()
async def main():
    msg = await get_data()
    await jk.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://api.sevin.cn/api/jk.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.strip()
    return data
