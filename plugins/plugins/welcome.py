from nonebot import on_notice
from nonebot.adapters.onebot.v11 import (
    Bot, 
    Message, 
    GroupIncreaseNoticeEvent
)
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent


welcome = on_notice()


@welcome.handle()
async def main(bot: Bot, event: GroupIncreaseNoticeEvent):
    user = event.get_user_id()
    at_ = "欢迎：[CQ:at,qq={}]".format(user)
    msg = at_ + f'加入！我是机器人{list(bot.config.nickname)[0]}，发送“菜单”查看我的详细功能或者@我和我聊天吧！'
    msg = Message(msg)
    await welcome.finish(message=Message(msg))
