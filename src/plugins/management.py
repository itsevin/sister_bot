from nonebot import on_command, on_request
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, GroupRequestEvent
import warnings
from nonebot.permission import *
import re


warnings.filterwarnings('ignore')

qtk = on_command('开启全禁')
qtg = on_command('关闭全禁')
jy = on_command('禁')
jj = on_command('解')
group_remove = on_command('踢')
agree_apply = on_command('同意申请')
disagree_apply = on_command('拒绝申请')
group_sq = on_request()
zr = 2720269770


@qtk.handle()
async def j(bot: Bot, event: GroupMessageEvent, state: T_State):
    group = event.group_id
    qq = event.user_id
    if qq == zr:
        await bot.set_group_whole_ban(group_id=group, enable=True)
        await qtk.finish(message=f'妹妹已经为您开启全体禁言了')
    else:
        await qtk.finish(message=f'你没有资格命令我！')


@qtg.handle()
async def g(bot: Bot, event: GroupMessageEvent, state: T_State):
    group = event.group_id
    qq = event.user_id
    try:
        if qq == zr:
            await bot.set_group_whole_ban(group_id=group, enable=False)
            await qtg.finish(message=f'妹妹已经为您关闭全体禁言了')
        else:
            await qtg.finish(message=f'你没有资格命令我！')
    except IndexError:
        print('error')


@jy.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        data = str(event.message)
        qq2 = event.user_id
        qq = re.findall(r'qq=(.+?)]', data)
        qq = int(qq[0])
        sj1 = re.findall(r'] (.+)', data)
        sj = sj1[0]
        sj = int(sj) * 60
        if qq2 == zr:
            await bot.set_group_ban(group_id=event.group_id, user_id=qq, duration=sj)
            await jy.finish(message=f'妹妹已禁言\nQQ:{qq}\n时间：{sj1[0]}分钟')
        else:
            await jy.finish(message=f'你没有资格命令我！')
    except IndexError:
        print('Error')


@jj.handle()
async def sj(bot: Bot, event: GroupMessageEvent, state: T_State):
    try:
        data = str(event.message)
        qq2 = event.user_id
        qq = re.findall(r'qq=(.+?)]', data)
        qq = int(qq[0])
        if qq2 == zr:
            await bot.set_group_ban(group_id=event.group_id, user_id=qq, duration=0)
            await jj.finish(message=f'妹妹已解除禁言\nQQ:{qq}')
        else:
            await jj.finish(message=f'你没有资格命令我！')
    except IndexError:
        print('Error')


@group_sq.handle()
async def sq(bot: Bot, event: GroupRequestEvent, state: T_State):
    qq_id = event.user_id
    message = event.comment  # 获取验证信息
    global flag_id
    flag_id = event.flag  # 申请进群的flag
    global type_id
    type_id = event.sub_type  # 请求信息的类型
    await group_sq.finish(message=f'有人申请进群\nQQ:{qq_id}\n验证消息:{message}\n同意/拒绝申请')


@agree_apply.handle()
async def sn(bot: Bot, event: GroupMessageEvent, state: T_State):
    if event.sender.role == "admin" or event.sender.role == "owner":
        await bot.set_group_add_request(flag=flag_id, sub_type=type_id, approve=True)
    else:
        await agree_apply.finish(message=f'对不起，你没有权限')


@disagree_apply.handle()
async def sn(bot: Bot, event: GroupMessageEvent, state: T_State):
    if event.sender.role == "admin" or event.sender.role == "owner":
        await bot.set_group_add_request(flag=flag_id, sub_type=type_id, approve=False, reason='机器人自动审批，如有误判请联系群主或其他管理员')
    else:
        await disagree_apply.finish(message=f'对不起，你没有权限')


@group_remove.handle()
async def move(bot: Bot, event: GroupMessageEvent, state: T_State):
    async def group_admin(event: GroupMessageEvent) -> bool:
        return event.sender.role == "admin"

    async def group_owner(event: GroupMessageEvent) -> bool:
        return event.sender.role == "owner"

    print(group_admin(event))
    if event.sender.role == "admin" or event.sender.role == "owner":
        data = str(event.message)
        group_id = event.group_id
        qq_id = re.findall(r'qq=(.+?)]', data)
        qq_id = qq_id[0]
        await bot.set_group_kick(group_id=group_id, user_id=qq_id, reject_add_request=False)
        await group_remove.finish(message=f'已将QQ:{qq_id}移除群聊')
    else:
        await group_remove.finish(message=f'对不起，你没有权限')
