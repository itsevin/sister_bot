from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx
import json
import re


sjgq = on_command(
    '随机歌曲',
    block=True,
    priority=11
)


@sjgq.handle()
async def main():
    get_music = await get_data()
    await sjgq.finish(get_music)


async def get_data():
    url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_json = json.loads(resp.text)
    get_dt = get_json['data']
    url = get_dt['url']
    url = re.findall(r'id=(.+?)$', url)
    data = MessageSegment.music(type_='163', id_=url[0])
    return data
