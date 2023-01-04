from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


tgrj = on_command('舔狗日记')


@tgrj.handle ()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await tgrj.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/tgrj.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text
    resp.close()
    return data
