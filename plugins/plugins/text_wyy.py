from nonebot import on_command
import httpx


wyyrp = on_command(
    '网易云热评',
    block=True,
    priority=11
)


@wyyrp.handle()
async def main():
    msg = await get_data()
    await wyyrp.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-wangyiyunreping/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
