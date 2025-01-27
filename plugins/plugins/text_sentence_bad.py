from nonebot import on_command
import httpx
import random
import json
import re


ktff = on_command(
    '口吐芬芳',
    block=True,
    priority=11
)


@ktff.handle()
async def main():
    msg = await get_data()
    await ktff.finish(msg)


async def get_data():
    url = f'https://v.api.aa1.cn/api/api-wenan-ktff/index.php?type={str(random.randint(1,5))}'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        text = re.search(r'\{\s*"code":\s*\d+,\s*"text":\s*".*?"\s*\}', resp.text.replace("\n", ""), re.S).group()
        get_dic = json.loads(text)
    data = get_dic["text"]
    return data
