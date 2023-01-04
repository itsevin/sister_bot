from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


zywa = on_command('中英文案')


@zywa.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await zywa.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-yingwen/index.php?type=text'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    resp.close()
    return data
