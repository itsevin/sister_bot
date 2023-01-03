from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot
import requests


djt = on_command('毒鸡汤')


@djt.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data()
    await djt.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-wenan-dujitang/index.php?aa1=text'
    resp = requests.get(url, headers=headers, timeout=1)
    data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
