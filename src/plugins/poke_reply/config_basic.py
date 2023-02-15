from nonebot import on_regex
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from typing import Callable
import json
import os.path
import aiofiles
import pydantic
from nonebot import logger
from pydantic import BaseModel


@on_regex("^重载配置$", permission=SUPERUSER).handle()
async def _(matcher: Matcher):
    await matcher.send("请稍候")
    try:
        await reload()
    except:
        logger.exception("配置重载失败")
        await matcher.finish("操作失败，请检查后台输出")
    else:
        await matcher.finish("操作完毕")


_tmp = []


def _model_to_object(model):
    if isinstance(model, BaseModel):
        return model.dict()
    elif isinstance(model, (list, tuple, set)):
        return [(x.dict() if isinstance(x, BaseModel) else x) for x in model]
    return model


class BaseConfig:

    def __init__(self, filename, model=None, default_conf=None):
        self._filename = filename
        self._model = model
        self._default_conf = default_conf
        self._tmp = None
        self._path = self._get_path()

    async def get(self):
        if not self._tmp:
            try:
                cf = await self.load()
                if self._model:
                    if isinstance(cf, dict):
                        self._tmp = self._model(**cf)
                    elif isinstance(cf, list):
                        self._tmp = [self._model(**x) for x in cf]
                    else:
                        raise TypeError("Type not supported")
                else:
                    self._tmp = cf
            except (pydantic.ValidationError, json.JSONDecodeError) as e:
                logger.exception("配置文件格式错误")
                raise e

        return self._tmp

    async def load(self):
        if not os.path.exists(self._path):
            conf = self._default_conf
        else:
            async with aiofiles.open(self._path, encoding="utf-8") as f:
                conf = json.loads(await f.read())

            if isinstance(conf, dict) and isinstance(self._default_conf, dict):
                # 将未配置的配置项配置为默认
                for k, v in self._default_conf.items():
                    if k not in conf:
                        conf[k] = v

        await self.save(conf)  # format / write default
        logger.debug(f'Loaded config "{self._filename}": {conf}')
        return conf

    async def save(self, custom_conf=None):
        async with aiofiles.open(self._path, "w", encoding="utf-8") as f:
            await f.write(
                json.dumps(
                    _model_to_object(custom_conf or self._tmp),
                    indent=2,
                    ensure_ascii=False,
                )
            )

    def clear_tmp(self):
        self._tmp = None

    def _get_path(self):
        fpath = os.path.join("shigure", f"{self._filename}.json")
        dir_name = os.path.dirname(fpath)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        return fpath

    def _check_tmp_is_list(self):
        if not isinstance(self._tmp, list):
            raise TypeError("Operation does not correspond to type")

    def _check_tmp_is_model(self):
        if not isinstance(self._tmp, BaseModel):
            raise TypeError("Operation does not correspond to type")

    def __getattr__(self, item):
        if isinstance(item, str) and item.startswith("_"):
            return self.__dict__[item]
        else:
            return getattr(self._tmp, item)

    def __setattr__(self, key, value):
        if isinstance(key, str) and key.startswith("_"):
            self.__dict__[key] = value
        else:
            self._check_tmp_is_model()
            setattr(self._tmp, key, value)

    def __getitem__(self, item):
        try:
            return self.__getattr__(item)
        except TypeError:
            self._check_tmp_is_list()
            return self._tmp.__getitem__(item)

    def __setitem__(self, key, value):
        try:
            self.__setattr__(key, value)
        except TypeError:
            self._check_tmp_is_list()
            self._tmp.__setitem__(key, value)

    def __len__(self):
        self._check_tmp_is_list()
        return len(self._tmp)

    def __iter__(self):
        self._check_tmp_is_list()
        yield from self._tmp


async def init(
    filename: str,
    model: Callable[[...], BaseModel] = None,
    default_conf: dict | list = None,
    cls: Callable[..., BaseConfig] = None,
):
    if cls:
        conf = cls(filename, model, default_conf)
    else:
        conf = BaseConfig(filename, model, default_conf)
    _tmp.append(conf)
    await conf.get()
    return conf


async def reload():
    for cf in _tmp:
        cf.clear_tmp()
        await cf.get()