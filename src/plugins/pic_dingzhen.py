from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests


dingzhen = on_command('丁真')


@dingzhen.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await dingzhen.finish(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/dingzhen.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.strip()
    resp.close()
    return data
