from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


fy = on_command('翻译')


@fy.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip().strip('翻译')
    msg = await get_data(get_msg)
    await fy.finish(msg)


async def get_data(get_msg):
    headers = {'Connection': 'close'}
    url = f'http://hm.suol.cc/API/fy.php?msg={get_msg}'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text
    resp.close()
    return data
