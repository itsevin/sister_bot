from nonebot import on_command
import httpx
import json


twqh = on_command(
    '土味情话',
    block=True,
    priority=11
)


@twqh.handle()
async def main():
    msg = await get_data()
    await twqh.finish(msg)


async def get_data():
    url = 'https://api.uomg.com/api/rand.qinghua?format=json'
    async with httpx.AsyncClient(timeout=30) as client:
        resp = await client.get(url)
        get_json = json.loads(resp.text)
    data = get_json['content']
    return data
