from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Bot, Event
import requests
import json


chat = on_command('*')


@chat.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip().strip('*')
    msg = get_data(get_msg)
    await chat.finish(msg)


def get_data(get_msg):
    headers = {'Connection': 'close'}
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={get_msg}'
    resp = requests.get(url, headers=headers, timeout=1)
    get_dic = json.loads(resp.text)
    data = get_dic['content'].replace('菲菲', '妹妹')
    return data
