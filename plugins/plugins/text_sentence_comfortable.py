from nonebot import on_command
import httpx


awwa = on_command(
    '安慰文案',
    block=True,
    priority=11
)


@awwa.handle()
async def main():
    msg = await get_data()
    await awwa.finish(msg)


async def get_data():
    url = 'https://v.api.aa1.cn/api/api-wenan-anwei/index.php?type=text'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        data = resp.text.replace("<p>", "").replace("</p>", "")
    return data
