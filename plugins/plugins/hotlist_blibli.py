from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Event,
    Message
)
import httpx
import json


bzrb = on_command(
    'b站热榜',
    block=True,
    priority=11
)


@bzrb.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip()
    if get_msg == "b站热榜":
        msg = await get_datas()
        await bzrb.finish(msg)
    else:
        try:
            get_msg = int(get_msg.strip('b站热榜').strip("+").strip())
        except:
            await bzrb.finish("请使用正确格式，请发送“b站热榜”获取功能说明")
        if get_msg >= 1:
            msg = await get_data(get_msg)
            await bzrb.finish(msg)
        else:
            await bzrb.finish("请使用正确格式，请发送“b站热榜”获取功能说明")


async def get_datas():
    url = 'https://api.vvhan.com/api/hotlist?type=bili'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    datas = "b站热榜："
    for i in range(0, 10):
        datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["title"]
    datas = datas + "\n（查看详情请输入”b站热榜+编号“）"
    return datas


async def get_data(get_msg):
    get_msg = int(get_msg) - 1
    url = 'https://api.vvhan.com/api/hotlist?type=bili'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    pic = get_list[get_msg]["pic"]
    title = get_list[get_msg]["title"]
    hot = get_list[get_msg]["hot"]
    url = get_list[get_msg]["url"]
    desc = get_list[get_msg]["desc"]
    if get_msg <= 9:
        data = Message(f"[CQ:image,file={pic}]\n标题：{title}\n介绍：{desc}\n热度：{hot}\n链接：{url}")
    else:
        data = "编号超出最大范围"
    return data
