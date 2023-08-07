from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx
import json


wbrb = on_command(
    '微博热榜',
    block=True,
    priority=11
)


@wbrb.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip()
    if get_msg == "微博热榜":
        msg = await get_datas()
        await wbrb.finish(msg)
    else:
        try:
            get_msg = int(get_msg.strip('微博热榜').strip("+").strip())
        except:
            await wbrb.finish("请使用正确格式，请发送“微博热榜”获取功能说明")
        if get_msg >= 1:
            msg = await get_data(get_msg)
            await wbrb.finish(msg)
        else:
            await wbrb.finish("请使用正确格式，请发送“微博热榜”获取功能说明")


async def get_datas():
    url = 'https://api.sevin.cn/api/hotlist.php?type=weibo'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    datas = "微博热榜："
    for i in range(0, 10):
        datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["title"]
    datas = datas + "\n（查看详情请输入”微博热榜+编号“）"
    return datas


async def get_data(get_msg):
    get_msg = int(get_msg) - 1
    url = 'https://api.sevin.cn/api/hotlist.php?type=weibo'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]
    if get_msg <= 9:
        data = "标题：" + get_list[get_msg]["title"] + "\n热度：" + get_list[get_msg]["hot"] + "\n链接：" + get_list[get_msg]["url"]
    else:
        data = "编号超出最大范围"
    return data
