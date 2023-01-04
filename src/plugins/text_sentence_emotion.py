from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


qgyy = on_command('情感一言')


@qgyy.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await qgyy.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-qg/index.php?aa1=text'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    resp.close()
    return data
