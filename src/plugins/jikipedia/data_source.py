import asyncio

import aiohttp
from nonebot.adapters.onebot.v11 import Message, MessageSegment

from .data_types import JikiResponse

SEARCH_URL = "https://api.jikipedia.com/go/search_entities"
HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8",
    "Client": "web",
    "Client-Version": "2.7.2g",
    "Connection": "keep-alive",
    # 'Content-Length'    : '38',
    # 'Content-Type'      : 'application/json;charset=UTF-8',
    "Host": "api.jikipedia.com",
    "Origin": "https://jikipedia.com",
    "Referer": "https://jikipedia.com/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "Token": "",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36",
    # todo: 逆向xid生成方式
    "XID": "uNo5bL1nyNCp/Gm7lJAHQ91220HLbMT8jqk9IJYhtHA4ofP+zgxwM6lSDIKiYoppP2k1IW/1Vxc2vOVGxOOVReebsLmWPHhTs7NCRygfDkE=",
    "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": '"Android"',
}


async def get_img_msg(url):
    try:
        async with aiohttp.ClientSession() as s:
            async with s.get(url) as r:
                return MessageSegment.image(await r.read())
    except:
        return MessageSegment.text(f"获取图片失败（{url}）")


async def get_geng_ret(name):
    async with aiohttp.ClientSession() as s:
        async with s.post(
            SEARCH_URL, headers=HEADERS, json={"phrase": name, "page": 1, "size": 60}
        ) as r:
            rj = await r.json()
            # logger.debug(f'\n{json.dumps(rj, ensure_ascii=False, indent=2)}')
            return JikiResponse(**rj)


def filter_definitions(data):
    tmp = []
    for da in data.data:
        tmp.extend(da.definitions)
    return tmp


async def format_definition(item):
    img = (
        await asyncio.gather(
            *[
                asyncio.create_task(get_img_msg(i))
                for i in [n.full.path for n in item.images]
            ]
        )
        if item.images
        else None
    )
    text = item.plaintext.replace("\u200b", "").replace("\u200c", "")
    tags = (
        " ".join([f"#{x}" for x in [y.name for y in item.tags]])
        if item.tags
        else "该词条还没有Tag哦～"
    )

    im = Message()
    im += f"词条【{item.term.title}】：\n"
    im += f"{text}\n"
    if img:
        im.extend(img)
    im += "\n"
    im += f"Tags：{tags}\n"
    im += f"原文：https://jikipedia.com/definition/{item.id}"
    return im
