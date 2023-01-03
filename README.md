<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="http://img.sevin.cn/i/2023/01/02/63b234522695e.png" width="200" height="200" alt="不正经的妹妹"></a>
</p>

<div align="center">
    <h1 align="center">✨Sevin 不正经的妹妹</h1>
</div>

<p align="center">
	<!-- 文档 -->
	<a style="margin-inline:5px" target="_blank" href="https://bot.sevin.cn">
		<img src="https://img.shields.io/badge/文档-Docs-FDE6E0?style=flat&logo=Blogger" title="文档">
	</a>&emsp;
    <!-- GitHub主页 -->
	<a style="margin-inline:5px" target="_blank" href="https://github.com/itsevin/qqbot">
		<img src="https://img.shields.io/badge/GitHub-Home-blue?style=flat&logo=GitHub" title="Github主页">
	</a>&emsp;
	<!-- Gitee主页 -->
	<a style="margin-inline:5px" target="_blank" href="https://gitee.com/itsevin/qqbot">
		<img src="https://img.shields.io/badge/Gitee-Home-blue?style=flat&logo=Gitee" title="Gitee主页">
	</a>&emsp;
	<!-- py版本 -->
	<img src="https://img.shields.io/badge/python-3.8+-blue" alt="python">
    <!-- nonebot版本 -->
    <a style="margin-inline:5px" target="_blank" href="https://github.com/nonebot/nonebot2/releases/tag/v2.0.0-beta.5">
		<img src="https://img.shields.io/badge/Nonebot-2.0.0b5-blue" title="nonebot2">
	</a>&emsp;
    <!-- go-cqhttp版本 -->
    <a style="margin-inline:5px" target="_blank" href="https://github.com/Mrs4s/go-cqhttp">
		<img src="https://img.shields.io/badge/gocqhttp-latest-blue" title="go-cqhttp">
	</a>&emsp;
</p>

## 描述

一款基于[NoneBot2](https://v2.nonebot.dev/)的QQ机器人，适配器为OneBot V11(使用其他的适配器请自行修改源码)

## 基本功能

- 音乐系统：点歌、随机歌曲
- 游戏系统：人生重开系统、扫雷系统、塔罗牌系统、猜单词系统、猜成语系统
- 视频系统：小姐姐视频
- 图片系统：二次元图、随机壁纸、4k壁纸、壁纸、看腿、鬼刀、灵梦、丁真、cosplay、jk
- 娱乐系统
  - 运势类：今日运势、星座运势
  - 文本类：顺口溜、毒鸡汤、随机一言、情感一言、安慰文案、骚话文案、中英文案、伤感语录、土味情话、舔狗日记、讲个笑话、口吐芬芳、网易云热评、朋友圈一言
  - 新闻热榜类：知乎热榜、b站热榜、抖音热榜、微博热榜、百度热榜
  - 交互类：和我聊天
- 工具系统：疫情查询、天气查询、中英互译、qq估价
- 群管系统：全体禁言、单人禁言、移出群聊、入群申请
- 表情包系统：头像表情包、文字表情包
- 作者介绍
- 版权声明


## 基本功能展示
![主菜单](http://img.sevin.cn/i/2022/12/26/63a9b52c99aa7.png)

## 使用
1.参照[NoneBot2文档](https://v2.nonebot.dev/)安装nonebotv2.0.0-beta.5 （其他版本可能会使部分插件不兼容，可自行修改）及go-cqhttp等相应前置，并完成机器人相关配置

（可参考[Nonebot2机器人搭建教程](https://blog.csdn.net/weixin_46211269/article/details/123725706)）

2.将本仓库plugins内的所有文件下载至`./src/plugins`路径

3.通过指令下载来自NoneBot2商店的其他作者的插件，插件原贴：

```
https://github.com/bingganhe123/60s-
https://github.com/AquamarineCyan/nonebot-plugin-today-in-history
https://github.com/MinatoAquaCrews/nonebot_plugin_tarot
https://github.com/zjkwdy/nonebot_plugin_weather_lite
https://github.com/noneplugin/nonebot-plugin-minesweeper
https://github.com/noneplugin/nonebot-plugin-handle
https://github.com/noneplugin/nonebot-plugin-wordle
https://github.com/noneplugin/nonebot-plugin-remake
https://github.com/noneplugin/nonebot-plugin-petpet
https://github.com/noneplugin/nonebot-plugin-simplemusic
https://github.com/noneplugin/nonebot-plugin-memes
```

对应插件下载指令：（在Windows的cmd或者Linux的终端使用）

```
nb plugin install nonebot-plugin-read-60s
nb plugin install nonebot-plugin-today-in-history
nb plugin install nonebot-plugin-tarot
nb plugin install nonebot-plugin-weather-lite
nb plugin install nonebot_plugin_minesweeper
nb plugin install nonebot_plugin_handle
nb plugin install nonebot_plugin_wordle
nb plugin install nonebot_plugin_remake
nb plugin install nonebot_plugin_petpet
nb plugin install nonebot_plugin_simplemusic
nb plugin install nonebot_plugin_memes
```

这里只提供下载指令，并标明原帖地址，插件有问题请去原贴提交issue

4.参照下面在配置文件`.env`中添加
```
# 今日60s插件配置
history_qq_friends=[] # 要发送的QQ好友
history_qq_groups=[863549352,856909552] # 要发送的群
history_inform_time=[{"HOUR":9,"MINUTE":1}] # 发送的时间点
# 在输入时间的时候不要以0开头如{"HOUR":06,"MINUTE":08}是错误的

# 历史上的今天插件配置
read_qq_friends=[] # 要发送的QQ好友
read_qq_groups=[863549352,856909552] # 要发送的群
read_inform_time=[{"HOUR":10,"MINUTE":1}] # 发送的时间点
# 在输入时间的时候不要以0开头如{"HOUR":06,"MINUTE":08}是错误的

# 设置超级管理员qq账号
SUPERUSERS=["2720269770"]

# 塔罗牌配置（不用改）
TAROT_PATH="./data/tarot/"
CHAIN_REPLY=false
```

5.如果是Ubuntu系统，则需下载相应中文字体。

在终端输入以下命令

```
sudo apt install fonts-noto
sudo locale-gen zh_CN zh_CN.UTF-8
sudo update-locale LC_ALL=zh_CN.UTF-8 LANG=zh_CN.UTF-8
fc-cache -fv
```

6.启动机器人
## 鸣谢

1.仓库内插件作者：[Sevin](https://home.sevin.cn)，[萌新源](https://gitee.com/meng-xinyuan-mxy)

3.仓库内插件调用的所有API：

```
https://api.sevin.cn/
https://api.juncikeji.xyz/
https://api.aai.cn/
https://api.vvhan.com/
https://api.uomg.com/
http://api.qingyunke.com/
http://hm.suol.cc/
http://81.70.100.130/
```

3.本机器人用到的来自[Nonebot2商店](https://v2.nonebot.dev/store)的其他插件的作者（具体见上）

4.[Nonebot2项目](https://github.com/nonebot/nonebot2)和[go-cqhttp项目](https://github.com/Mrs4s/go-cqhttp)

## 友链
1.另一款QQ机器人：[辞辞配置](https://gitee.com/yevin_bot/cici-bot)

---

PS：如果你觉得这个机器人还不错的话就给个star吧 QWQ
