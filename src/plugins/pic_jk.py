from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, MessageSegment
import requests


jk = on_command('jk')


@jk.handle ()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await jk.send(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/jk.php'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.strip()
    return data
