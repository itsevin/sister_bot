# 安装go-cqhttp

## go-cqhttp 是什么？

使用OneBot协议实现的无头QQ，接受消息发往后端处理，实现了机器人实现收发消息的功能

## 怎么安装？

### 下载

从[Mrs4s / go-cqhttp](https://github.com/Mrs4s/go-cqhttp)的[Release](https://github.com/Mrs4s/go-cqhttp/releases)中下载与你系统对应的最新版本

> 如果你是Windows: 一般是下载 `go-cqhttp_windows_amd64.zip`

###  配置

1. 解压后会得到`go-cqhttp`，首次运行会让你选择通信方式，选择 `3` (反向 Websocket 通信)，会生成一个配置文件**config.yml**

![](https://itsevin.github.io/sister_bot/#/install/1.png)

2. 在**config.yml**文件中，将uin修改为bot账号，password修改为密码（留空就是扫码登录，登录方式按实际情况选择）。

3. 在**config.yml**文件中，将
   `universal: ws://your_websocket_universal.server`
   修改为
   `universal: ws://127.0.0.1:8080/onebot/v11/ws/`
   
   > 这里的8080指的是你机器人的端口，与等会配置的机器人端口需要一致。一般使用8080，如果有端口冲突可修改。

### 启动

再次启动go-cqhttp后会自动生成设备信息文件**device.json**，里面的**protocol**配置的是机器人登录设备，默认的6是apad，如果登不上可以自行更换设备（范围为1-6，自行尝试）

然后再根据终端提示进行操作，登上账号即可

> 想要机器人工作，就要go-cqhttp成功登上账号并且保持程序运行

## 登不上怎么办？

- 仔细查看[go-cqhttp的issues](https://github.com/Mrs4s/go-cqhttp/issues)，并尝试解决问题
- 加群问群友（请先尝试自行解决）

