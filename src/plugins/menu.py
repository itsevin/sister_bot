from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event
import random


cd = on_command('菜单')
bqbxt = on_command('表情包系统')
ylxt = on_command('娱乐系统')
tpxt = on_command('图片系统')
spxt = on_command('视频系统')
gjxt = on_command('工具系统')
yxxt = on_command('游戏系统')
yyxt = on_command('音乐系统')
qgxt = on_command('群管系统')
zzjs = on_command('作者介绍')
bqsm = on_command('版权声明')
bqbhc = on_command('表情包合成')
hwlt = on_command('和我聊天')
xzys = on_command('星座运势')
zyhy = on_command('中英互译')
yqcx = on_command('疫情查询')
tqcx = on_command('天气查询')
qndxxxt = on_command('青年大学习系统')
xxch = on_command('消息撤回')
dmyx = on_command('代码运行')
rsck = on_command('人生重开系统')
slxt = on_command('扫雷系统')
tlpxt = on_command('塔罗牌系统')
cdcxt = on_command('猜单词系统')
ccyxt = on_command('猜成语系统')
gjqlxt = on_command('国际棋类系统')
xqxt = on_command('象棋系统')
mgxt = on_command('迷宫系统')
ysl = on_command('运势类')
wbl = on_command('文本类')
xwrbl = on_command('新闻热榜类')
jhl = on_command('交互类')
dg = on_command('点歌')


@cd.handle()  # 菜单响应体
async def main():
    data = "—☃—不正经的妹妹—☃—\n♚♚♚表情包系统♚♚♚\n♚音乐系统♚游戏系统♚\n♚视频系统♚图片系统♚\n♚娱乐系统♚工具系统♚\n♚群管系统♚作者介绍♚\n♚版权声明♚敬请期待♚\n————————————\n❤  不正经的妹妹  ❤\n防封编码："
    data += str(random.randint(10000, 99999))
    await cd.finish(data)


@ylxt.handle()  # 娱乐系统响应体
async def main():
    data = "娱乐系统:\n1、运势类\n2、文本类\n3、新闻热榜类\n4、交互类\n防封编码："
    data += str(random.randint(10000, 99999))
    await ylxt.finish(data)


@ysl.handle()  # 运势类响应体
async def main():
    data = "运势类：\n1、今日运势\n2、星座运势\n防封编码："
    data += str(random.randint(10000, 99999))
    await ysl.finish(data)


@wbl.handle()  # 文本类响应体
async def main():
    data = "♚随机一言♚情感一言♚\n♚安慰文案♚骚话文案♚\n♚中英文案♚伤感语录♚\n♚土味情话♚舔狗日记♚\n♚讲个笑话♚口吐芬芳♚\n♚网易云热评♚顺口溜♚\n♚朋友圈一言♚毒鸡汤♚\n防封编码："
    data += str(random.randint(10000, 99999))
    await wbl.finish(data)


@xwrbl.handle()  # 新闻热榜类响应体
async def main():
    data = "新闻热榜类：\n1、知乎热榜\n2、b站热榜\n3、抖音热榜\n4、微博热榜\n5、百度热榜\n防封编码："
    data += str(random.randint(10000, 99999))
    await xwrbl.finish(data)


@jhl.handle()  # 交互类响应体
async def main():
    data = "交互类：\n1、和我聊天\n2、语音聊天\n防封编码："
    data += str(random.randint(10000, 99999))
    await jhl.finish(data)


@tpxt.handle()  # 图片系统响应体
async def main():
    data = "1.二次元图\n2.随机壁纸\n3.4k壁纸\n4.壁纸\n5.看腿\n6.鬼刀\n7.灵梦\n8.丁真\n9.cosplay\n10.jk\n防封编码："
    data += str(random.randint(10000, 99999))
    await tpxt.finish(data)


@spxt.handle()  # 视频系统响应体
async def main():
    data = "1.小姐姐视频\n2.敬请期待\n防封编码："
    data += str(random.randint(10000, 99999))
    await tpxt.finish(data)


@gjxt.handle()  # 工具系统响应体
async def main():
    data = "1.青年大学习系统\n2.疫情查询\n3.天气查询\n4.中英互译\n5.qq估价\n6.消息撤回\n7.代码运行\n防封编码："
    data += str(random.randint(10000, 99999))
    await gjxt.finish(data)


@yyxt.handle()  # 音乐系统响应体
async def main():
    data = "1.点歌\n2.随机歌曲\n防封编码："
    data += str(random.randint(10000, 99999))
    await gjxt.finish(data)


@yxxt.handle()  # 游戏系统响应体
async def main():
    data = "1.人生重开系统\n2.扫雷系统\n3.塔罗牌系统\n4.猜单词系统\n5.猜成语系统\n6.国际棋类系统\n7.象棋系统\n8.迷宫系统\n防封编码："
    data += str(random.randint(10000, 99999))
    await gjxt.finish(data)


@bqbxt.handle()  # 表情包系统响应体
async def main():
    data = "1.头像表情包\n2.文字表情包\n3.表情包合成\nPS：\n输入上面的指令获取表情包模板\n头像表情包例子：“吃 @网安社”\n文字表情包例子：“鲁迅说 我没说过这句话”\n防封编码："
    data += str(random.randint(10000, 99999))
    await bqbxt.finish(data)


@qgxt.handle()  # 群管系统响应体
async def main():
    data = "#全体禁言\n1.开启全禁\n2.关闭全禁\n#单人禁言\n1.禁@某人 禁言时间（单位：分钟）\n2.解@某人\n#移出群聊\n1.踢@某人\n#入群申请\n1.同意申请\n2.拒绝申请\n防封编码："
    data += str(random.randint(10000, 99999))
    await qgxt.finish(data)


@zzjs.handle()  # 作者介绍响应体
async def main():
    data = "机器人作者：ITSevin\n作者QQ：2720269770\n作者主页：home.sevin.cn\n防封编码："
    data += str(random.randint(10000, 99999))
    await zzjs.finish(data)


@bqsm.handle()  # 版权声明响应体
async def main():
    data = "机器人作者：Sevin\n机器人开源地址：\ngitee.com/itsevin/botplugins\n机器人有问题请联系作者\n或者通过提交issues\n防封编码："
    data += str(random.randint(10000, 99999))
    await bqsm.finish(data)


@bqbhc.handle()  # 表情包合成响应体
async def main():
    data = "触发示例：😎+😁=？\n防封编码："
    data += str(random.randint(10000, 99999))
    await bqbhc.finish(data)


@hwlt.handle()  # 和我聊天响应体
async def main():
    data = "输入“*”加你要和我聊的内容\n防封编码："
    data += str(random.randint(10000, 99999))
    await hwlt.finish(data)


@xzys.handle()  # 星座运势响应体
async def main():
    data = "输入“星座+星座名”,如“星座天蝎座”\n防封编码："
    data += str(random.randint(10000, 99999))
    await xzys.finish(data)


@zyhy.handle()  # 中英互译响应体
async def main():
    data = "输入“翻译+文本”，如“翻译你好，世界”，语种将会自动识别\n防封编码："
    data += str(random.randint(10000, 99999))
    await zyhy.finish(data)


@yqcx.handle()  # 疫情查询响应体
async def main():
    data = "输入“疫情+地域（县级以上）”，如:“疫情泉州”\n防封编码："
    data += str(random.randint(10000, 99999))
    await yqcx.finish(data)


@tqcx.handle()  # 天气查询响应体
async def main():
    data = "输入“天气+城市名”，如:“天气泉州”\n防封编码："
    data += str(random.randint(10000, 99999))
    await tqcx.finish(data)


@qndxxxt.handle()  # 青年大学习系统响应体
async def main():
    data = "输入“青年大学习”获取大学习答案\n输入“开启大学习推送”开启推送，仅限私聊\n输入“大学习截图”获取主页截图\n输入”完成截图“获取大学习完成截图\n防封编码："
    data += str(random.randint(10000, 99999))
    await qndxxxt.finish(data)


@xxch.handle()  # 消息撤回响应体
async def main():
    data = "对我的消息回复“撤回”可帮我撤回不合适的言论喔\n防封编码："
    data += str(random.randint(10000, 99999))
    await xxch.finish(data)


@dmyx.handle()  # 代码运行响应体
async def main():
    data = "指令如下\ncode [语言] [-i] [inputText]\n-i：可选输入 后跟输入内容\n运行代码示例(python)(无输入)\n    code py        \nprint('你好')\n运行代码示例(python)(有输入)：\n    code py -i 你好\n        print(input())\n防封编码："
    data += str(random.randint(10000, 99999))
    await dmyx.finish(data)


@dg.handle()  # 点歌响应体
async def main(event: Event):
    if str(event.get_message()).strip() == "点歌":
        data = "输入“点歌“或”qq点歌“或”网易点歌“或”酷我点歌“或”酷狗点歌“或”咪咕点歌“或”b站点歌”+关键词，如:“qq点歌反方向的钟”\n防封编码："
        data += str(random.randint(10000, 99999))
        await dg.finish(data)


@rsck.handle()  # 人生重开系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 人生重开“\n防封编码："
    data += str(random.randint(10000, 99999))
    await slxt.finish(data)


@slxt.handle()  # 扫雷系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 扫雷（初级/中级/高级）“\n挖开方块输入“挖开+位置”（可同时指定多个位置）\n标记方块输入“标记+位置”（可同时指定多个位置）\n位置为“字母+数字”，如“A1”\n添加人员到游戏内输入“添加人员+@某人”（只能当前局内玩家进行添加）\n防封编码："
    data += str(random.randint(10000, 99999))
    await slxt.finish(data)


@tlpxt.handle()  # 塔罗牌系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 占卜”\n得到单张塔罗牌回应输入“@不正经的妹妹 塔罗牌”\n防封编码："
    data += str(random.randint(10000, 99999))
    await tlpxt.finish(data)


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


@xqxt.handle()  # 象棋系统响应体
async def main():
    data = "开始游戏输入“@不正经的妹妹 象棋人机/象棋对战”\n可使用“lv1~8”指定AI等级，如“象棋人机lv5”，默认为“lv4”\n发送 中文纵线格式如“炮二平五” 或 起始坐标格式如“h2e2”下棋\n发送“结束下棋”结束当前棋局\n发送“显示棋盘”显示当前棋局\n发送“悔棋”可进行悔棋（人机模式可无限悔棋,对战模式只能撤销自己上一手下的棋）\n防封编码："
    data += str(random.randint(10000, 99999))
    await xqxt.finish(data)


@mgxt.handle()  # 迷宫系统响应体
async def main():
    data = "使用以下命令开始游戏，需加上命令前缀！\nmaze [-r --rows <ROWS>] [-c --cols <COLUMNS>] [-m --method <ALGORITHM>]\n可使用-r规定迷宫的行数，-c规定迷宫的列数\n可使用-m规定迷宫的生成算法，目前支持DFS，Prim，Kruskal三种算法，默认值为Kruskal\n开始游戏后需要持续发送操作序列以在迷宫中移动，直到解开迷宫\n操作格式为“方向+步数”，方向分上下左右，步数为1表示一个方向走到尽头，不填步数为走1步，其余步数正常\n操作序列就是多个操作写在一起\n游戏中可以输入“结束“或”quit“退出游戏并获取参考解法\n防封编码："
    data += str(random.randint(10000, 99999))
    await mgxt.finish(data)
