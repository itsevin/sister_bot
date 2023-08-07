from nonebot import on_command
import httpx
import json


bdrb = on_command(
    '百度热榜',
    block=True,
    priority=11
)


@bdrb.handle()
async def main():
    msg = await get_data()
    await bdrb.finish(msg)


async def get_data():
    url = 'https://api.sevin.cn/api/hotlist.php?type=baidu'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    get_list = get_dic["data"]["cards"][0]["content"]
    datas = "百度热榜："
    for i in range(0, 15):
        if get_list[int(i)]["desc"] != "":
            datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["desc"]
        else:
            datas = datas + "\n" + str(int(i) + 1) + "." + get_list[int(i)]["query"]
    return datas
