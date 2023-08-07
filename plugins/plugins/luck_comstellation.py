from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import httpx


xz = on_command(
    '星座',
    block=True,
    priority=11
)


@xz.handle()
async def main(event: Event):
    get_msg = str(event.get_message()).strip().strip('星座').strip()
    if get_msg != "运势":
        msg = await get_data(get_msg)
        await xz.finish(msg)


async def get_data(get_msg):
    url = f'http://hm.suol.cc/API/xzys.php?msg={get_msg}'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text
    html = '{br}'
    n = '\n'
    if html in data:
        data = data.replace(html, n)
    return data
