from nonebot import on_command
import httpx
import re


pyqyy = on_command(
    '朋友圈一言',
    block=True,
    priority=11
)


@pyqyy.handle()
async def main():
    msg = await get_data()
    await pyqyy.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/pyq/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        match = re.search(r'<p>(.*?)</p>', resp.text, re.DOTALL)
        data = match.group(1).strip()
    return data
