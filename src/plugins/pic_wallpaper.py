from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests
import json


sjbz = on_command('随机壁纸')


@sjbz.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_pic()
    await sjbz.finish(MessageSegment.image(msg))


async def get_pic():
    headers = {'Connection': 'close'}
    url = 'https://api.vvhan.com/api/bing?type=json&rand=sj'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic1 = json.loads(resp.text)
    get_dic2 = get_dic1["data"]
    data = get_dic2["url"]
    resp.close()
    return data
