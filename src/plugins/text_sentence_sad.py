from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message
import requests


sgyl = on_command('伤感语录')


@sgyl.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await sgyl.send(Message(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'http://api.sevin.cn/api/sgyl.php'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text
    return data
