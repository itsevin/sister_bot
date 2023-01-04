from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State
import requests
import json


dyrb = on_command('抖音热榜')


@dyrb.handle()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip()
    if get_msg == "抖音热榜":
        msg = get_datas()
        await dyrb.finish(msg)
    else:
        try:
            get_msg = int(get_msg.strip('抖音热榜').strip("+").strip())
        except:
            await dyrb.finish(Message("请使用正确格式，请发送“抖音热榜”获取功能说明"))
        if get_msg >= 1:
            msg = await get_data(get_msg)
            await dyrb.finish(msg)
        else:
            await dyrb.finish(Message("请使用正确格式，请发送“抖音热榜”获取功能说明"))


def get_datas():
    headers = {'Connection': 'close'}
    url = 'https://api.vvhan.com/api/hotlist?type=douyinHot'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    datas = "抖音热榜："
    for i in range(0, 10):
        datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["title"]
    datas = datas + "\n（查看详情请输入”抖音热榜+编号“）"
    resp.close()
    return datas


async def get_data(get_msg):
    get_msg = int(get_msg) - 1
    headers = {'Connection': 'close'}
    url = 'https://api.vvhan.com/api/hotlist?type=douyinHot'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    if get_msg <= 9:
        data = Message("标题：" + get_list[get_msg]["title"] + "\n热度：" + get_list[get_msg]["hot"] + "\n链接：" + get_list[get_msg]["url"])
    else:
        data = "编号超出最大范围"
    resp.close()
    return data
