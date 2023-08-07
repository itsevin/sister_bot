from nonebot import on_command
import httpx


sgyl = on_command(
    '伤感语录',
    block=True,
    priority=11
)


@sgyl.handle()
async def main():
    msg = await get_data()
    await sgyl.finish(msg)


async def get_data():
    url = 'https://api.sevin.cn/api/sgyl.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text
    return data
