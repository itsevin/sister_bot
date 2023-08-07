from nonebot import on_command
import httpx


djt = on_command(
    '毒鸡汤',
    block=True,
    priority=11
)


@djt.handle()
async def main():
    msg = await get_data()
    await djt.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-dujitang/index.php?aa1=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
