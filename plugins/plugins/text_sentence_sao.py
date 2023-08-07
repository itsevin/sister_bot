from nonebot import on_command
import httpx


shwa = on_command(
    '骚话文案',
    block=True,
    priority=11
)


@shwa.handle()
async def main():
    msg = await get_data()
    await shwa.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-saohua/index.php?type=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
