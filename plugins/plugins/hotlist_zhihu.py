from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Event,
    Message
)
import httpx
import json


zhrb = on_command(
    '知乎热榜',
    block=True,
    priority=11
)


@zhrb.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip()
    if get_msg == "知乎热榜":
        msg = await get_datas()
        await zhrb.finish(msg)
    else:
        try:
            get_msg = int(get_msg.strip('知乎热榜').strip("+").strip())
        except:
            await zhrb.finish(Message("请使用正确格式，请发送“知乎热榜”获取功能说明"))
        if get_msg >= 1:
            msg = await get_data(get_msg)
            await zhrb.finish(msg)
        else:
            await zhrb.finish(Message("请使用正确格式，请发送“知乎热榜”获取功能说明"))


async def get_datas():
    url = 'https://api.sevin.cn/api/hotlist.php?type=zhihu'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    datas = "知乎热榜："
    for i in range(0, 10):
        datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["title"]
    datas = datas + "\n（查看详情请输入”知乎热榜+编号“）"
    return datas


async def get_data(get_msg):
    get_msg = int(get_msg) - 1
    url = 'https://api.sevin.cn/api/hotlist.php?type=zhihu'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    pic = get_list[get_msg]["pic"]
    title = get_list[get_msg]["title"]
    hot = get_list[get_msg]["hot"]
    url = get_list[get_msg]["url"]
    if get_msg <= 9:
        data = Message(f"[CQ:image,file={pic}]\n标题：{title}\n热度：{hot}\n链接：{url}")
    else:
        data = "编号超出最大范围"
    return data
