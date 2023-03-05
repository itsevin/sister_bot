from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx


fy = on_command(
    '翻译',
    block=True,
    priority=11
)


@fy.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip().strip('翻译')
    msg = await get_data(get_msg)
    await fy.finish(msg)


async def get_data(get_msg):
    url = f'http://hm.suol.cc/API/fy.php?msg={get_msg}'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.text
    return data
