import asyncio

from pydantic import BaseModel

from .._config import init

config = None


class ConfigModel(BaseModel):
    send_suggestion: bool
    suggestion_num: int


async def update_conf():
    global config
    config = await init(
        "jikipedia", ConfigModel, {"send_suggestion": True, "suggestion_num": 3}
    )


asyncio.run(update_conf())
