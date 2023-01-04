from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


awwa = on_command('安慰文案')


@awwa.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await awwa.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=text'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    resp.close()
    return data
