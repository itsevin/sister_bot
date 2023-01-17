from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx
import json


chat = on_command('*')


@chat.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip().strip('*')
    msg = await get_data(get_msg)
    await chat.finish(msg)


async def get_data(get_msg):
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={get_msg}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    data = get_dic['content'].replace('菲菲', '妹妹')
    return data
