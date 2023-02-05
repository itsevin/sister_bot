import asyncio
import os
from typing import Literal, Optional

from nonebot import logger
from pydantic import BaseModel

from .._config import BaseConfig, init

config = None


class Config(BaseConfig):
    async def get(self):
        if not self._tmp:
            tmp = await super(Config, self).get()
            for i in tmp.copy():
                if i.type == "image_folder":
                    tmp.remove(i)
                    for n in find_all_file(i.content):
                        tmp.append(
                            ConfigModel(type="image", content=n, action=i.action)
                        )
                elif i.type == "texts":
                    tmp.remove(i)
                    for n in i.content:
                        tmp.append(ConfigModel(type="text", content=n, action=i.action))
            logger.debug(f"Parsed config: {tmp}")
            self._tmp = tmp
        return self._tmp


class ConfigModel(BaseModel):
    type: Literal["text", "image", "texts", "image_folder"]
    content: str | list[str]
    action: Optional[bool]


def find_all_file(base):
    li = []
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            li.append(fullname)
    return li


async def update_conf():
    global config
    config = await init("poke_replies", ConfigModel, [], cls=Config)


asyncio.run(update_conf())
