from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, Bot, MessageSegment
import requests


kt = on_command('看腿')


@kt.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    await kt.finish("此功能仅限于私聊，请加好友使用")


@kt.handle()
async def main(bot: Bot, event: PrivateMessageEvent, state: T_State):
    msg = await get_pic()
    await kt.finish(MessageSegment.image(msg))


async def get_pic():
    headers = {'Connection': 'close'}
    url = 'http://81.70.100.130/api/tu.php'
    resp = requests.get(url, headers=headers, timeout=3)
    data = resp.text.replace("\n", "").strip()
    resp.close()
    return data
