from nonebot import on_command
import httpx


zywa = on_command(
    '中英文案',
    block=True,
    priority=11
)


@zywa.handle()
async def main():
    msg = await get_data()
    await zywa.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-yingwen/index.php?type=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
