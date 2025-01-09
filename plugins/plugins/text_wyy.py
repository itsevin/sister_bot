from nonebot import on_command
import httpx
import re


wyyrp = on_command(
    '网易云热评',
    block=True,
    priority=11
)


@wyyrp.handle()
async def main():
    msg = await get_data()
    await wyyrp.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-wangyiyunreping/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        match = re.search(r'<p>(.*?)</p>', resp.text, re.DOTALL)
        data = match.group(1).strip()
    return data
