from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests


wyyrp = on_command('网易云热评')


@wyyrp.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await wyyrp.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-wangyiyunreping/index.php?aa1=text'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    resp.close()
    return data
