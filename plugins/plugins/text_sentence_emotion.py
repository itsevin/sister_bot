from nonebot import on_command
import httpx
import re


qgyy = on_command(
    '情感一言',
    block=True,
    priority=11
)


@qgyy.handle()
async def main():
    msg = await get_data()
    await qgyy.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-qg/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        match = re.search(r'<p>(.*?)</p>', resp.text, re.DOTALL)
        data = match.group(1).strip()
    return data
