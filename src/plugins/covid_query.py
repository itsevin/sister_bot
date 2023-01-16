import json

import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Bot, Message
from nonebot.typing import T_State

yq = on_command('疫情')


@yq.handle ()
async def main(bot: Bot, event: Event, state: T_State):
    get_msg = str(event.get_message()).strip().strip('疫情').strip()
    if get_msg != "查询":
        msg = await get_data(get_msg)
        await yq.finish(Message(msg))


async def get_data(get_msg):
    headers = {'Connection': 'close'}
    url = f'https://api.juncikeji.xyz/api/yiqing.php?msg={get_msg}'
    resp = requests.get(url, headers=headers, timeout=3)
    get_dic = json.loads(resp.text)
    if get_dic["累计确诊"] != "null":
        data = "地区:"+get_msg+"\n累计确诊："+get_dic["累计确诊"]+"\n累计治愈："+get_dic["累计治愈"]+"\n累计死亡："+get_dic["累计死亡"]+"\n现存无症状："+get_dic["现存无症状"]+"\n累现存诊："+get_dic["现存确诊"]+"\n数据来源："+get_dic["数据来源"]
    else:
        data = "未查询到相关数据，请确认查询地区为国内合法省级或市级"
    resp.close()
    return data
