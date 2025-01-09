from nonebot import on_command
import httpx
import re


awwa = on_command(
    '安慰文案',
    block=True,
    priority=11
)


@awwa.handle()
async def main():
    msg = await get_data()
    await awwa.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        match = re.search(r'<p>(.*?)</p>', resp.text, re.DOTALL)
        data = match.group(1).strip()
    return data
