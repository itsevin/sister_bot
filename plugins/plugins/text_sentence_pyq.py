from nonebot import on_command
import httpx


pyqyy = on_command(
    '朋友圈一言',
    block=True,
    priority=11
)


@pyqyy.handle()
async def main():
    msg = await get_data()
    await pyqyy.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/pyq/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
