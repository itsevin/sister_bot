from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx
import json


sjbz = on_command(
    '随机壁纸',
    block=True,
    priority=11
)


@sjbz.handle()
async def main():
    msg = await get_pic()
    await sjbz.finish(MessageSegment.image(msg))


async def get_pic():
    url = 'https://api.vvhan.com/api/bing?type=json&rand=sj'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic1 = json.loads(resp.text)
    get_dic2 = get_dic1["data"]
    data = get_dic2["url"]
    return data
