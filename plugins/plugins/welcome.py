from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Message
from nonebot.adapters.onebot.v11 import GroupIncreaseNoticeEvent


welcome = on_notice()


@welcome.handle()
async def main(event: GroupIncreaseNoticeEvent):
    user = event.get_user_id()
    at_ = "欢迎：[CQ:at,qq={}]".format(user)
    msg = at_ + '加入！我是机器人不正经的妹妹，发送“菜单”查看我的详细功能或者@我和我聊天吧！'
    msg = Message(msg)
    await welcome.finish(message=Message(msg))
