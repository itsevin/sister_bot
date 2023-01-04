from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests
import re


wallpaper = on_command('4k壁纸')


@wallpaper.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await wallpaper.finish(MessageSegment.image(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://v.api.aa1.cn/api/api-fj-2/index.php?aa1=url'
    resp = requests.get(url, headers=headers, timeout=3)
    get_list = re.findall("//[\s\S]*$", resp.text.replace("\n", "").replace("\t", "").replace(" ", ""))
    data = "https:" + get_list[0]
    resp.close()
    return data
