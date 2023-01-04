from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event, MessageSegment
import requests
import json
import re


sjgq = on_command('随机歌曲')


@sjgq.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_music = await get_data()
    await sjgq.finish(get_music)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.uomg.com/api/rand.music?sort=热歌榜&format=json'
    resp = requests.get(url, headers=headers, timeout=3)
    get_json = json.loads(resp.text)
    get_dt = get_json['data']
    url = get_dt['url']
    url = re.findall(r'id=(.+?)$', url)
    data = MessageSegment.music(type_='163', id_=url[0])
    resp.close()
    return data
