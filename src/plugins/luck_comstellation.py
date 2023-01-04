from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, Message
import requests


xz = on_command ('星座')


@xz.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip().strip('星座').strip()
    if get_msg != "运势":
        msg = await get_data(get_msg)
        await xz.finish(Message(msg))


async def get_data(get_msg):
    headers = {'Connection': 'close'}
    url = f'http://hm.suol.cc/API/xzys.php?msg={get_msg}'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text
    html = '{br}'
    n = '\n'
    if html in data:
        data = data.replace(html, n)
    resp.close()
    return data
