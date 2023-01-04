from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Bot
import requests
import random
import json


ktff = on_command('口吐芬芳')


@ktff.handle()
async def main(bot: Bot, event: Event, state: T_State):
    msg = await get_data()
    await ktff.finish(msg)


async def get_data():
    headers = {'Connection': 'close'}
    url = f'https://v.api.aa1.cn/api/api-wenan-ktff/index.php?type={str(random.randint(1,5))}'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text.replace("\n", ""))
    data = get_dic["text"]
    resp.close()
    return data
