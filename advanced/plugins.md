# 自定义插件

## 说明

机器人启动时会自动加载自定义插件，并且更新时会自动处理不会覆盖

## 本地插件

自定义本地插件放在`plugins/extra_plugins`中

> 文件夹不存在就自己创建

## 商店插件

自定义商店插件需要在poetry中添加依赖并在虚拟环境中用nb指令安装插件，指令如下：

```bash
poetry add <插件pypi包名>
poetry run nb pugin add <商店插件名>
```

> 在nb指令前有`poetry run`是为了在虚拟环境中使用nb指令添加插件