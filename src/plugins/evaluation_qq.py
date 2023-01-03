from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message
import requests
import json


qqgj = on_command('qq估价')


@qqgj.handle()
async def main(bot: Bot, event: GroupMessageEvent, state: T_State):
    msg = await get_data(event.get_user_id())
    await qqgj.finish(Message(msg))


async def get_data(qq):
    headers = {'Connection': 'close'}
    url = f'https://v.api.aa1.cn/api/qqgj-v2/?qq={str(qq)}'
    resp = requests.get(url, headers=headers, timeout=1)
    get_dic = json.loads(resp.text)
    data = "QQ账号："+str(get_dic["qq"])+"\n位数："+str(get_dic["ws"])+"\n规律："+str(get_dic["gl"])+"\n价格："+str(get_dic["money"])
    return data
