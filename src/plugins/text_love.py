from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests
import json


twqh = on_command('土味情话')


@twqh.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await twqh.send ( Message ( msg ) )


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.uomg.com/api/rand.qinghua?format=json'
    resp = requests.get(url, headers=headers, timeout=1)
    get_json = json.loads(resp.text)
    data = get_json['content']
    return data
