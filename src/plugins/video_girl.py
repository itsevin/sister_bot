from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, PrivateMessageEvent, Bot, MessageSegment
import requests


xjjsp = on_command('小姐姐视频')


@xjjsp.handle ()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    await xjjsp.finish("此功能仅限于私聊，请加好友使用")


@xjjsp.handle ()
async def main(bot: Bot, event: PrivateMessageEvent, state: T_State):
    msg = await get_data()
    await xjjsp.finish(MessageSegment.video(msg))


async def get_data():
    headers = {'Connection': 'close'}
    url = 'https://tucdn.wpon.cn/api-girl/index.php?wpon=url'
    resp = requests.get(url, headers=headers, timeout=1)
    data = "https:" + resp.text.strip()
    return data
