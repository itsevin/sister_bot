# 安装机器人

## 安装Python（3.10+，推荐3.10版本）

Windows可从[官网](https://www.python.org/downloads/windows/)下载或者直接去微软商店下载

Linux可以参考：https://blog.csdn.net/weixin_43935402/article/details/121416812

## 安装机器人本体

###  下载源码

在[这里](https://github.com/itsevin/sister_bot/releases/latest)下载最新版本的源码包

> 不要下载 pre-release 版本！要下载旁边写了 latest 的版本

### 安装依赖

1. 解压后打开机器人主目录（主目录能看到 logo.png 文件），然后安装`poetry`

在终端输入

```
pip install poetry
```

> 如果你是大陆网络环境下载太慢可以输入这个指令更换镜像源：
> `pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/`

2. 安装依赖包

```
poetry install
```

> 安装失败可以多试几次

### 初始化

首次运行机器人以初始化机器人——生成配置及下载依赖和数据

```
poetry run nb run
```

等到运行的差不多了（几分钟），终端显示内容不再变化就可以关了
