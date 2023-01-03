from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests


shwa = on_command('骚话文案')


@shwa.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await shwa.send(Message(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-saohua/index.php?type=text'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
