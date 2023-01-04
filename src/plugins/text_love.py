from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests
import json


twqh = on_command('土味情话')


@twqh.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await twqh.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.uomg.com/api/rand.qinghua?format=json'
    resp = requests.get(url, headers=headers, timeout=3)
    get_json = json.loads(resp.text)
    data = get_json['content']
    resp.close()
    return data
