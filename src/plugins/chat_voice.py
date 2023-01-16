from nonebot.adapters.onebot.v11 import (
    Event,
    Bot
)
from nonebot import require
require('nonebot_plugin_record')
from nonebot_plugin_record import (
    on_record,
    get_text,
    record_tts
)

import httpx
import json


chat = on_record()


@chat.handle()
async def main(bot: Bot, event: Event):
    text = await get_text(bot, event)
    msg = await get_data(text)
    await chat.finish(record_tts(msg))


async def get_data(msg):
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={msg}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    data = get_dic['content']
    return data
