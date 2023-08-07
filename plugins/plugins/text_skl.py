from nonebot import on_command
import httpx


skl = on_command(
    '顺口溜',
    block=True,
    priority=11
)


@skl.handle()
async def main():
    msg = await get_data()
    await skl.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-shunkouliu/index.php?type=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
