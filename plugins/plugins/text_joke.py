from nonebot import on_command
import httpx


jgxh = on_command(
    '讲个笑话',
    block=True,
    priority=11
)


@jgxh.handle()
async def main():
    msg = await get_data()
    await jgxh.finish(msg)


async def get_data():
    url = 'https://api.sevin.cn/api/qwxh.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("\\n", "\n")
    return data
