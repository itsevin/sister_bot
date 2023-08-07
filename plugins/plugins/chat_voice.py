from nonebot.adapters.onebot.v11 import (
    GroupMessageEvent,
    PrivateMessageEvent,
    Event,
    Bot
)
from nonebot import (
    require,
    on_command
)
require('nonebot_plugin_record')
from nonebot_plugin_record import (
    on_record,
    get_text,
    record_tts
)
import httpx
import json


chat = on_record()
yylt = on_command(
    "语音聊天",
    block=True,
    priority=11
)


@yylt.handle()
async def main(event: GroupMessageEvent):
    await yylt.finish("此功能仅限于私聊，请加好友使用")


@yylt.handle()
async def main(event: PrivateMessageEvent):
    await yylt.finish("请发送语音，仅限普通话")


@chat.handle()
async def main(bot: Bot, event: Event):
    text = await get_text(bot, event)
    msg = await get_data(text)
    await chat.finish(record_tts(msg))


async def get_data(msg):
    url = f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={msg}'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_dic = json.loads(resp.text)
    data = get_dic['content']
    return data
