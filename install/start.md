# 持久化运行方案

## 说明

要使机器人工作就需要保持 go-cqhttp 和机器人程序的持续运行

Windows把程序挂在后台就可以了，Linux就需要一些特殊手段

## 即刻开始（以运行机器人程序，Ubuntu为例）

> 这只是一个简单的方案，如果你有更好的请跳过

1. 安装screen

   ```
   sudo apt install screen
   ```

2. 创建会话
   
   ```
   screen -S sister_bot
   ```
   
   > `sister_bot`为会话名，可以随便取
   
3. 进入机器人目录

   ```
   cd <实际的机器人目录>
   ```

4. 启动机器人
   ```
   poetry run nb run
   ```

5. 完成之后你再退出终端，程序仍会在后台运行，回到该终端的命令为`screen -r sister_bot`

> 别忘了也要使go-cqhttp持续运行

