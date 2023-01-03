from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests


jgxh = on_command('讲个笑话')


@jgxh.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await jgxh.send(Message(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/qwxh.php'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.replace("\\n", "\n")
    return data
