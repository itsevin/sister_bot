from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx
import json


qqgj = on_command(
    'qq估价',
    block=True,
    priority=11
)


@qqgj.handle()
async def main(event: Event):
    msg = await get_data(event.get_user_id())
    await qqgj.finish(msg)


async def get_data(qq):
    url = f'https://v.api.aa1.cn/api/qqgj-v2/?qq={str(qq)}'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
    get_dic = json.loads(resp.text)
    data = "QQ账号："+str(get_dic["qq"])+"\n位数："+str(get_dic["ws"])+"\n规律："+str(get_dic["gl"])+"\n价格："+str(get_dic["money"])
    return data
