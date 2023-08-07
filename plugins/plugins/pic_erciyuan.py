from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx


ecyt = on_command(
    '二次元图',
    block=True,
    priority=11
)


@ecyt.handle()
async def main():
    msg = await get_data()
    await ecyt.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://api.sevin.cn/api/ecy.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.strip()
    return data
