from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event
import random

cd = on_command(
    '菜单',
    aliases={'帮助', '功能', 'help', 'menu'},
    block=True,
    priority=10
)
rgzn = on_command(
    '人工智能',
    block=True,
    priority=10
)
ylxt = on_command(
    '娱乐系统',
    block=True,
    priority=10
)
tpxt = on_command(
    '图片系统',
    block=True,
    priority=10
)
gjxt = on_command(
    '工具系统',
    block=True,
    priority=10
)
yxxt = on_command(
    '游戏系统',
    block=True,
    priority=10
)
bqsm = on_command(
    '版权声明',
    block=True,
    priority=10
)
xzys = on_command(
    '星座运势',
    block=True,
    priority=10
)
tqcx = on_command(
    '天气查询',
    block=True,
    priority=10
)
mcfztcx = on_command(
    'mc服状态查询',
    block=True,
    priority=10
)
zzgj = on_command(
    '站长工具',
    block=True,
    priority=10
)
xxch = on_command(
    '消息撤回',
    block=True,
    priority=10
)
dmyx = on_command(
    '代码运行',
    block=True,
    priority=10
)
yyzh = on_command(
    '淫语转换',
    block=True,
    priority=10
)
rsck = on_command(
    '人生重开系统',
    block=True,
    priority=10
)
slxt = on_command(
    '扫雷系统',
    block=True,
    priority=10
)
cdcxt = on_command(
    '猜单词系统',
    block=True,
    priority=10
)
ccyxt = on_command(
    '猜成语系统',
    block=True,
    priority=10
)
gjqlxt = on_command(
    '国际棋类系统',
    block=True,
    priority=10
)
mgxt = on_command(
    '迷宫系统',
    block=True,
    priority=10
)
ysl = on_command(
    '运势类',
    block=True,
    priority=10
)
wbl = on_command(
    '文本类',
    block=True,
    priority=10
)
xwrbl = on_command(
    '新闻热榜类',
    block=True,
    priority=10
)


@cd.handle()  # 菜单响应体
async def main(bot: Bot):
    data = f"🌟 {list(bot.config.nickname)[0]}功能菜单 🌟\n\n🎨 表情包制作\n自动生成有趣的表情包\n🤖 人工智能\n和我聊天，了解我的AI能力\n🎮 游戏系统\n玩游戏，尽情娱乐\n🖼️ 图片系统\n浏览美图，享受视觉盛宴\n🎉 娱乐系统\n尽享快乐时光\n🛠️ 工具系统\n实用工具，帮助生活\n📜 版权声明\n了解机器人版权相关问题\n\n发送功能名称触发以功能\n在消息中@我和我聊天吧\n防封编码："
    data += str(random.randint(10000, 99999))
    await cd.finish(data)


@ylxt.handle()  # 娱乐系统响应体
async def main():
    data = "娱乐系统:\n1.运势类\n2.文本类\n3.新闻热榜类\n防封编码："
    data += str(random.randint(10000, 99999))
    await ylxt.finish(data)


@ysl.handle()  # 运势类响应体
async def main():
    data = "运势类：\n1.今日运势\n2.星座运势\n防封编码："
    data += str(random.randint(10000, 99999))
    await ysl.finish(data)


@wbl.handle()  # 文本类响应体
async def main():
    data = "✨随机一言✨情感一言✨\n✨安慰文案✨骚话文案✨\n✨中英文案✨伤感语录✨\n✨土味情话✨舔狗日记✨\n✨讲个笑话✨口吐芬芳✨\n✨网易云热评✨顺口溜✨\n✨朋友圈一言✨毒鸡汤✨\n防封编码："
    data += str(random.randint(10000, 99999))
    await wbl.finish(data)


@xwrbl.handle()  # 新闻热榜类响应体
async def main():
    data = "新闻热榜类：\n1.知乎热榜\n2.微博热榜\n3.百度热榜\n防封编码："
    data += str(random.randint(10000, 99999))
    await xwrbl.finish(data)


@tpxt.handle()  # 图片系统响应体
async def main():
    data = "1.二次元图\n2.随机壁纸\n3.4k壁纸\n4.壁纸\n5.鬼刀\n6.灵梦\n7.丁真\n8.cosplay\n9.jk\n防封编码："
    data += str(random.randint(10000, 99999))
    await tpxt.finish(data)


@rgzn.handle()  # 人工智能响应体
async def main():
    data = "发送“@机器人+消息”进行聊天\n发送“人格”可进行人格设定\nPS:聊天功能由ChatGpt3.5提供\n防封编码："
    data += str(random.randint(10000, 99999))
    await rgzn.finish(data)


@gjxt.handle()  # 工具系统响应体
async def main():
    data = "1.mc服状态查询\n2.天气查询\n3.消息撤回\n4.代码运行\n5.淫语转换\n防封编码："
    data += str(random.randint(10000, 99999))
    await gjxt.finish(data)


@yxxt.handle()  # 游戏系统响应体
async def main():
    data = "1.人生重开系统\n2.扫雷系统\n3.猜单词系统\n4.猜成语系统\n5.国际棋类系统\n6.迷宫系统\n防封编码："
    data += str(random.randint(10000, 99999))
    await yxxt.finish(data)


@bqsm.handle()  # 版权声明响应体
async def main():
    data = "机器人作者：ITSevin\n机器人开源地址：\nhttps://github.com/itsevin/sister_bot\n机器人有问题请联系作者\n或者通过提交issues\n防封编码："
    data += str(random.randint(10000, 99999))
    await bqsm.finish(data)


@xzys.handle()  # 星座运势响应体
async def main():
    data = "输入“星座+星座名”,如“星座天蝎座”\n防封编码："
    data += str(random.randint(10000, 99999))
    await xzys.finish(data)


@tqcx.handle()  # 天气查询响应体
async def main():
    data = "输入“天气+城市名”，如:“天气泉州”\n防封编码："
    data += str(random.randint(10000, 99999))
    await tqcx.finish(data)


@mcfztcx.handle()  # mc服状态查询响应体
async def main():
    data = "JE服务器状态查询指令：\n!motd <服务器 IP>[:端口]\nBE服务器状态查询指令：\n!motdpe <服务器 IP>[:端口]\nJE/BE服务器状态查询指令：\n!motdfull <服务器 IP>[:端口]\n防封编码："
    data += str(random.randint(10000, 99999))
    await mcfztcx.finish(data)


@zzgj.handle()  # 站长工具响应体
async def main():
    data = "指令：\n1.二维码解析 <附带或回复一张图片>\n2.二维码生成 <内容>\n3.ping <主机名>\n4.icp查询 <域名>\n5.拦截检测 <网址>\n6.sping <主机名> [节点数量]\n7.whois查询 <域名>\n防封编码："
    data += str(random.randint(10000, 99999))
    await zzgj.finish(data)


@xxch.handle()  # 消息撤回响应体
async def main():
    data = "对我的消息回复“撤回”可帮我撤回不合适的言论喔\n防封编码："
    data += str(random.randint(10000, 99999))
    await xxch.finish(data)


@dmyx.handle()  # 代码运行响应体
async def main():
    data = "指令如下\ncode [语言] [-i] [inputText]\n-i：可选输入 后跟输入内容\n运行代码示例(python)(无输入)\n    code py        \nprint('你好'),\n运行代码示例(python)(有输入)：\n    code py -i 你好\n        print(input())\n防封编码："
    data += str(random.randint(10000, 99999))
    await dmyx.finish(data)


@yyzh.handle()  # 淫语转换响应体
async def main():
    data = "指令：“淫语+要转换的句子+淫乱度（可选）”\n如：“淫语 不能再这样下去了啊 80%”\n防封编码："
    data += str(random.randint(10000, 99999))
    await yyzh.finish(data)


@rsck.handle()  # 人生重开系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 人生重开“\n防封编码："
    data += str(random.randint(10000, 99999))
    await rsck.finish(data)


@slxt.handle()  # 扫雷系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 扫雷（初级/中级/高级）“\n挖开方块输入“挖开+位置”（可同时指定多个位置）\n标记方块输入“标记+位置”（可同时指定多个位置）\n位置为“字母+数字”，如“A1”\n添加人员到游戏内输入“添加人员+@某人”（只能当前局内玩家进行添加）\n防封编码："
    data += str(random.randint(10000, 99999))
    await slxt.finish(data)


@ccyxt.handle()  # 猜成语系统响应体
async def main():
    data = "开始游戏输入：“@不正经的妹妹 猜成语”\n游戏规则：\n你有十次的机会猜一个四字词语\n每次猜测后，汉字与拼音的颜色将会标识其与正确答案的区别\n青色 表示其出现在答案中且在正确的位置\n橙色 表示其出现在答案中但不在正确的位置\n当四个格子都为青色时，你便赢得了游戏！\n可发送“结束”结束游戏\n可发送“提示”查看提示\n防封编码："
    data += str(random.randint(10000, 99999))
    await ccyxt.finish(data)


@cdcxt.handle()  # 猜单词系统响应体
async def main():
    data = "开始游戏输入：“@不正经的妹妹 猜单词”\n游戏规则：\n绿色块代表此单词中有此字母且位置正确\n黄色块代表此单词中有此字母，但该字母所处位置不对\n灰色块代表此单词中没有此字母\n猜出单词或用光次数则游戏结束\n可发送“结束”结束游戏\n可发送“提示”查看提示\n高级玩法：\n可使用 -l / --length 指定单词长度，默认为 5\n可使用 -d / --dic 指定词典，默认为 CET4\n支持的词典：GRE、考研、GMAT、专四、TOEFL、SAT、专八、IELTS、CET4、CET6\n防封编码："
    data += str(random.randint(10000, 99999))
    await cdcxt.finish(data)


@gjqlxt.handle()  # 国际棋类系统响应体
async def main():
    data = "棋类：五子棋、围棋（禁全同，暂时不支持点目）、黑白棋\n开始游戏输入：“@不正经的妹妹+棋类”,一个群内同时只能有一个棋局\n发送“落子 字母+数字”下棋，如“落子 A1”\n游戏发起者默认为先手，可使用 --white 选项选择后手\n发送“结束下棋”结束当前棋局\n发送“查看棋局”显示当前棋局\n发送“悔棋”可以进行悔棋\n发送“跳过回合”可跳过当前回合（仅黑白棋支持）\n手动结束游戏或超时结束游戏时，可发送“重载xx棋局”继续下棋，如:重载围棋棋局\n防封编码："
    data += str(random.randint(10000, 99999))
    await gjqlxt.finish(data)


@mgxt.handle()  # 迷宫系统响应体
async def main():
    data = "使用以下命令开始游戏，需加上命令前缀！\nmaze [-r --rows <ROWS>] [-c --cols <COLUMNS>] [-m --method <ALGORITHM>]\n可使用-r规定迷宫的行数，-c规定迷宫的列数\n可使用-m规定迷宫的生成算法，目前支持DFS，Prim，Kruskal三种算法，默认值为Kruskal\n开始游戏后需要持续发送操作序列以在迷宫中移动，直到解开迷宫\n操作格式为“方向+步数”，方向分上下左右，步数为1表示一个方向走到尽头，不填步数为走1步，其余步数正常\n操作序列就是多个操作写在一起\n游戏中可以输入“结束“或”quit“退出游戏并获取参考解法\n防封编码："
    data += str(random.randint(10000, 99999))
    await mgxt.finish(data)
