from nonebot import on_command
import httpx


qgyy = on_command(
    'ζζδΈθ¨',
    block=True,
    priority=11
)


@qgyy.handle()
async def main():
    msg = await get_data()
    await qgyy.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-qg/index.php?aa1=text'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
