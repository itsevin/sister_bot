from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, MessageSegment
import requests


guidao = on_command('鬼刀')


@guidao.handle ()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await guidao.send(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/guidao.php'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.strip()
    return data
