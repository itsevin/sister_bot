from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Bot
from nonebot.typing import T_State
import requests
import json


bdrb = on_command('百度热榜')


@bdrb.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = get_data()
    await bdrb.finish(msg)


def get_data():
    headers = {'Connection': 'close'}
    url = 'https://api.sevin.cn/api/hotlist.php?type=baidu'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text)
    get_list = get_dic["data"]["cards"][0]["content"]
    datas = "百度热榜："
    for i in range(0, 15):
        if get_list[int(i)]["desc"] != "":
            datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["desc"]
        else:
            datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["query"]
    resp.close()
    return datas
