from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


jgxh = on_command('讲个笑话')


@jgxh.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await jgxh.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/qwxh.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("\\n", "\n")
    resp.close()
    return data
