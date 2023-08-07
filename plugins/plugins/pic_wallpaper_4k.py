from nonebot import on_command
from nonebot.adapters.onebot.v11 import MessageSegment
import httpx
import re


wallpaper = on_command(
    '4k壁纸',
    block=True,
    priority=11
)


@wallpaper.handle()
async def main():
    msg = await get_data()
    await wallpaper.finish(MessageSegment.image(msg))


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-fj-2/index.php?aa1=url'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_list = re.findall("//[\s\S]*$", resp.text.replace("\n", "").replace("\t", "").replace(" ", ""))
    data = "https:" + get_list[0]
    return data
