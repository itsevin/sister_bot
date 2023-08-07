from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx


lm = on_command(
    '灵梦',
    block=True,
    priority=11
)


@lm.handle()
async def main():
    msg = await get_data()
    await lm.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://api.sevin.cn/api/lingmeng.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.strip()
    return data
