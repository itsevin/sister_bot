from nonebot import on_command
import httpx


sjyy = on_command(
    '随机一言',
    block=True,
    priority=11
)


@sjyy.handle()
async def main():
    msg = await get_data()
    await sjyy.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/yiyan/index.php'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
