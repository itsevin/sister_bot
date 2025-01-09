from nonebot import on_command
import httpx
import re


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
        match = re.search(r'<p>(.*?)</p>', resp.text, re.DOTALL)
        data = match.group(1).strip()
    return data
