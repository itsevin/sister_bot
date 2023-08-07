from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx


guidao = on_command(
    '鬼刀',
    block=True,
    priority=11
)


@guidao.handle()
async def main():
    msg = await get_data()
    await guidao.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://api.sevin.cn/api/guidao.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.strip()
    return data
