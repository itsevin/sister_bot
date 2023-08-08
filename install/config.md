# 配置机器人

## 填写机器人配置

打开`config/bot_config/cinfig.yaml`，按照格式填写配置

### 配置项说明

- BOT_UPDATE
  - AUTO_UPDATE
    类型：bool
    默认值：true
    说明：是否自动更新
  - AUTO_RESETART
    类型：bool
    默认值：true
    说明：更新完毕是否自动重启
- PROXY
  - PROXY 
    类型：str
    默认值：None
    说明： 机器人使用的代理
- RELEASES
  - RELEASES
    类型：str
    默认值：stable
    范围：stable或者dev
    说明：使用的机器人版本

> 请使用stable版本，dev版本仅供作者测试使用

## 填写nonebot配置和插件配置

打开`env.dev`，按照注释填写配置

## 代理配置说明

本机器人的不同功能有不同的网络环境要求，并且有其自己的代理配置项：

- 机器人本体（本页有配置说明的）：能够稳定访问GitHub，非大陆代理即可
- nonebot_plugin_natural_gpt（聊天功能）：能够稳定访问OpenAi并且ip归属地在ChatGpt可用范围地区（如：台湾，美国，新加坡）
- 其他大部分需要使用代理的插件：非大陆代理即可

所以如果你是非大陆网络环境，只要考虑第二点的代理即可；

如果你是大陆网络环境，可以选择全部使用符合所有要求的代理，或者只考虑第一点和第三点的代理，第二点通过配置API请求地址为其他的能够稳定访问的反向代理地址解决而不使用代理

> 反向代理地址如： https://openai-proxy-api.pages.dev/api