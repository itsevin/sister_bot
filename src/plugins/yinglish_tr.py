import re

import yinglish
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg


@on_command("淫语", block=True, priority=11).handle()
async def _(matcher: Matcher, arg: Message = CommandArg()):
    if arg := arg.extract_plain_text().strip():
        lvl = 0.5
        arg_li = arg.split(" ")

        if sex_lvl := re.match("(-?\d{1,3}(\.\d+)?)%", arg_li[-1]):
            lvl = float(sex_lvl[1])
            if lvl <= 0:
                return await matcher.finish("不！够！涩！！（淫乱度不能低于或等于0%）", at_sender=True)
            if lvl > 100:
                return await matcher.finish(
                    "要……要坏掉惹❤呜咿——！（淫乱度不能大于100%）", at_sender=True
                )

            arg = " ".join(arg_li[:-1])
            lvl /= 100

        ret = yinglish.chs2yin(arg, lvl)
        await matcher.finish(f" {ret}", at_sender=True)

    await matcher.finish("啊呜……你不明所以的话我会很困扰的说：\n请输入“淫语+要转换的语句”以将语句淫荡化", at_sender=True)
