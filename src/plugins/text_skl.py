from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests


skl = on_command('顺口溜')


@skl.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await skl.send(Message(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-shunkouliu/index.php?type=text'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
