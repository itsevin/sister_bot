from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests


lm = on_command('灵梦')


@lm.handle ()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await lm.finish(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/lingmeng.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.strip()
    resp.close()
    return data
