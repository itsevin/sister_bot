from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, MessageSegment
import requests


cosplay = on_command('cosplay')


@cosplay.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await cosplay.send(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/cos.php'
    reso = requests.get(url, headers=headers, timeout=1)
    data = reso.text.strip()
    return data
