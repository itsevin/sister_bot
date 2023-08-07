from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx
import json


fy = on_command(
    '翻译',
    block=True,
    priority=11
)


@fy.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip().strip('翻译')
    msg = await get_data(get_msg)
    await fy.finish(msg)


async def get_data(get_msg):
    url = f'https://api.vvhan.com/api/fy?text={get_msg}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    data = get_dic["data"]["fanyi"]
    return data
