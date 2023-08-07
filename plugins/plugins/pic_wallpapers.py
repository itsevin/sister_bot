from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    MessageSegment,
    Event
)
import httpx
import random
import json


wallpaper = on_command(
    '壁纸',
    block=True,
    priority=11
)


@wallpaper.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip("壁纸").strip()
    if get_msg != "随机" and get_msg != "4k" and get_msg != "":
        msg = await get_data(get_msg)
        await wallpaper.finish(MessageSegment.image(msg))
    elif get_msg == "":
        msg = "输入“壁纸+类型”获取相应类型壁纸，如“壁纸美女”\n可选类型：美女，爱情，风景，清新，动漫，明星，萌宠，游戏，汽车，时尚，日历，影视，军事，体育，萌娃，格言\n防封编码："
        msg += str(random.randint(10000, 99999))
        await wallpaper.finish(msg)


async def get_data(get_msg):
    url = f'https://v.api.aa1.cn/api/bz-v2/?msg={get_msg}'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_url = get_dic["pctu_url"]
    if get_url != "":
        data = get_url
    else:
        data = "请输入正确分类名称，如：“美女壁纸”\n具体分类项请输入“壁纸”获取"
    return data
