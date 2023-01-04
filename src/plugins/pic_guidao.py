from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests


guidao = on_command('鬼刀')


@guidao.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await guidao.finish(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/guidao.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.strip()
    resp.close()
    return data
