from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot, MessageSegment
import requests
import random
import json


wallpaper = on_command('壁纸')


@wallpaper.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip("壁纸").strip()
    if get_msg != "随机" and get_msg != "4k" and get_msg != "":
        msg = await get_data(get_msg)
        await wallpaper.finish(MessageSegment.image(msg))
    elif get_msg == "":
        msg = "输入“壁纸+类型”获取相应类型壁纸，如“壁纸美女”\n可选类型：美女，爱情，风景，清新，动漫，明星，萌宠，游戏，汽车，时尚，日历，影视，军事，体育，萌娃，格言\n防封编码："
        msg += str(random.randint(10000, 99999))
        await wallpaper.finish(msg)


async def get_data(get_msg):
    headers = {'Connection': 'close'}
    url = f'https://v.api.aa1.cn/api/bz-v2/?msg={get_msg}'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text)
    get_url = get_dic["pctu_url"]
    if get_url != "":
        data = get_url
    else:
        data = "请输入正确分类名称，如：“美女壁纸”\n具体分类项请输入“壁纸”获取"
    resp.close()
    return data
