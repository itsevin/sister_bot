from nonebot import on_command
import httpx


tgrj = on_command('舔狗日记')


@tgrj.handle ()
async def main():
    msg = await get_data()
    await tgrj.finish(msg)


async def get_data():
    url = 'https://api.sevin.cn/api/tgrj.php'
    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        data = resp.text
    return data
