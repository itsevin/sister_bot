from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, MessageSegment
import requests


dingzhen = on_command('丁真')


@dingzhen.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await dingzhen.send(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/dingzhen.php'
    resp = requests.get(url, timeout=1, headers=headers)
    data = resp.text.strip()
    return data
