from pathlib import Path
from typing import Any, Dict, Optional, Type

import builtins
from nonebot import logger
from pydantic import BaseModel
from ruamel import yaml
from ruamel.yaml import YAML
from ruamel.yaml.scanner import ScannerError
import ujson as json


class Config(BaseModel):
    """
    配置项
    """

    value: Any
    """配置项值"""
    help_: Optional[str]
    """配置注解"""
    default_value: Optional[Any] = None
    """默认值"""
    type_: Any = None
    """参数类型"""


class ConfigGroup(BaseModel):
    """
    配置组
    """

    module: str
    """模块名"""
    configs: Dict[str, Config] = {}
    """配置项列表"""


class ConfigsManager:
    """
    插件配置 与 资源 管理器
    """

    def __init__(self, yaml_name: str):
        self._data: Dict[str, ConfigGroup] = {}
        self._file = yaml_name
        self._user_file_path = Path() / "config" / "bot_config" / f"{self._file}.yaml"
        self._full_file_path = Path() / "config" / "bot_config" / "complete" / f"{self._file}.yaml"
        self.load_data()

    def add_plugin_config(
        self,
        module: str,
        key: str,
        value: Optional[Any],
        help_: Optional[str] = None,
        default_value: Optional[Any] = None,
        type_: Optional[Type] = None,
        _override: bool = False,
        auto_save: bool = True,
    ):
        """
        添加一个配置，配置值不会被覆盖
        :param module: 模块
        :param key: 键
        :param value: 值
        :param help_: 配置注解
        :param default_value: 默认值
        :param type_: 类型
        :param _override: 强制覆盖值
        :param auto_save: 自动保存
        """
        module = module.upper()
        key = key.upper()
        if module in self._data and (config := self._data[module].configs.get(key)):
            config.default_value = default_value
            config.help_ = help_
            config.type_ = type_
            if _override:
                config.value = value
        else:
            key = key = key.upper()
            if not self._data.get(module):
                self._data[module] = ConfigGroup(module=module)
            self._data[module].configs[key] = Config(
                value=value,
                help_=help_,
                default_value=default_value,
                type_=type_,
            )
        if auto_save:
            self.save_data()
    
    def delete_plugin_config(
        self,
        module: str,
        key: str,
        auto_save: bool = True,
    ):
        """
        添加一个配置，配置值不会被覆盖
        :param module: 模块
        :param key: 键
        :param auto_save: 自动保存
        """
        module = module.upper()
        key = key.upper()
        if module in self._data and key in self._data[module].configs:
            del self._data[module].configs[key]
            if not self._data[module].configs: 
                del self._data[module]
            if auto_save:
                self.save_data()

    def set_config(
        self,
        module: str,
        key: str,
        value: Any,
        auto_save: bool = True,
    ):
        """
        设置配置值
        :param module: 模块名
        :param key: 配置名称
        :param value: 值
        :param auto_save: 自动保存
        """
        module = module.upper()
        key = key.upper()
        if module in self._data and key in self._data[module].configs:
            if self._data[module].configs[key].value != value:
                self._data[module].configs[key].value = value
                if auto_save:
                    self.save_data()
        else:
            logger.error(f"未查询到配置项 MODULE: [ {module} ] | KEY: [ {key} ] ，无法设置配置值")

    def get_config(
        self, 
        module: str, 
        key: str,
    ) -> Optional[Any]:
        """
        获取指定配置 Config
        :param module: 模块名
        :param key: 配置名称
        """
        module = module.upper()
        key = key.upper()
        logger.debug(
            f"尝试获取配置 MODULE: [ {module} ] | KEY: [ {key} ]"
        )
        key = key = key.upper()
        if module in self._data.keys() and (config := self._data[module].configs.get(key)):
            logger.debug(
                f"获取配置 MODULE: [ {module} ] | KEY: [ {key} ] 成功"
            )
            return config
        else:
            logger.error(
                f"未查询到配置项 MODULE: [ {module} ] | KEY: [ {key} ] ，无法获取配置"
            )

    def get_value(
        self, 
        module: str, 
        key: str, 
        default: Optional[Any] = None
    ) -> Optional[Any]:
        """
        获取指定配置值
        :param module: 模块名
        :param key: 配置名称
        :param default: 没有key值内容的默认返回值
        """
        module = module.upper()
        key = key.upper()
        logger.debug(
            f"尝试获取配置 MODULE: [ {module} ] | KEY: [{key}]"
        )
        value = None
        if module in self._data.keys():
            config = self._data[module].configs.get(key)
            if not config:
                logger.error(
                    f"未查询到配置项 MODULE: [ {module} ] | KEY: [ {key} ] ，无法获取配置值"
                )
            else:
                try:
                    if config.value:
                        if config.type_:
                            type_obj = getattr(builtins, config.type_)
                            value = type_obj(config.value)
                        else:
                            value = config.value
                    elif config.default_value:
                        if config.type_:
                            type_obj = getattr(builtins, config.type_)
                            value = type_obj(config.default_value)
                        else:
                            value = config.default_value
                except Exception as e:
                    logger.warning(
                        f"配置项类型转换失败 MODULE: [ {module} ] | KEY: [ {key} ]",
                        e=e,
                    )
                    value = config.value or config.default_value
        if value is None:
            value = default
        logger.debug(
            f"获取配置 MODULE: [ {module} ] | KEY: [ {key} ] -> [ {value} ]"
        )
        return value

    def generate_default(self):
        """
        生成默认完整配置文件
        """  
        template_file = Path() / "source" / "config" / f"{self._file}.json"
        with open(template_file, "r", encoding="utf-8") as f:
            template = json.load(f)
        for module, configs in template.items():
            for key, config in configs.items():
                self.add_plugin_config(
                    module=module,
                    key=key, 
                    type_=config["type"],
                    default_value=config["default_value"],
                    value=config["value"],
                    help_=config["help"]
                )
        logger.info(f"完整配置文件 {self._file}.yaml 生成成功")

    def save_user_data(self):
        """
        保存用户配置至用户配置文件
        """
        user_data = {}
        for module, config_group in self._data.items():
            for key, config in config_group.configs.items():
                user_data.setdefault(module, {})[key] = config.value
        with open(self._user_file_path, "w", encoding="utf-8") as f:
            yaml.dump(
                user_data, 
                f, 
                indent=2, 
                Dumper=yaml.RoundTripDumper, 
                allow_unicode=True
            )

    def save_full_data(self):
        """
        保存完整配置至完整配置文件
        """
        full_data = {}
        for module, config_group in self._data.items():
            for key, config in config_group.configs.items():
                full_data.setdefault(module, {})[key] = config.dict()
        with open(self._full_file_path, "w", encoding="utf-8") as f:
            yaml.dump(
                full_data, 
                f, 
                indent=2, 
                Dumper=yaml.RoundTripDumper, 
                allow_unicode=True
            )

    def save_data(self):
        """
        保存配置文件
        """
        self.save_full_data()
        self.save_user_data()

    def reload(self):
        """
        重新加载配置文件
        """
        logger.debug(f"开始重新加载配置文件 {self._file}.yaml ")
        self.load_data()

    def load_user_data(self):
        """
        从用户配置文件加载数据
        """
        with open(self._user_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content:
            logger.warning(f"用户配置文件 {self._file}.yaml 为空，开始从完整配置文件恢复用户配置文件")
            self.save_user_data()
            logger.info(f"用户配置文件 {self._file}.yaml 恢复成功")
        _yaml = YAML()
        try:
            with open(self._user_file_path, "r", encoding="utf-8") as f:
                user_data = _yaml.load(f)
        except ScannerError as e:
            raise ScannerError(
                    f"{e}\n**********************************************\n"
                    f"** 可能为用户配置文件 {self._file}.yaml 填写不规范 *\n"
                    f"**********************************************"
                )
        count = 0
        for module, configs in user_data.items():
            for key, value in configs.items():
                self.set_config(
                    module, 
                    key, 
                    value, 
                    auto_save=False
                )
                count += 1
        logger.debug(f"加载用户配置完成，共加载 {len(user_data)} 个配置组及对应 {count} 个配置项")

    def load_full_data(self):
        """
        从完整配置文件加载数据
        """
        with open(self._full_file_path, "r", encoding="utf-8") as f:
            content = f.read()
        if not content:
            logger.error(f"完整配置文件 {self._file}.yaml 为空，开始生成默认完整配置文件")
            self.generate_default()
            logger.info(f"默认完整配置文件 {self._file}.yaml 生成成功")
        _yaml = YAML()
        try:
            with open(self._full_file_path, "r", encoding="utf-8") as f:
                full_data = _yaml.load(f)
        except ScannerError as e:
            raise ScannerError(
                    f"{e}\n**********************************************\n"
                    f"** 可能为完整配置文件 {self._file}.yaml 填写不规范 *\n"
                    f"**********************************************"
                )
        count = 0
        for module, configs in full_data.items():
            for key, config in configs.items():
                self.add_plugin_config(
                    module=module,
                    key=key,
                    value=config["value"],
                    help_=config["help_"],
                    default_value=config["default_value"],
                    type_=config["type_"],
                    auto_save=False,
                )
                count += 1
        logger.debug(f"加载完整配置完成，共加载 {len(full_data)} 个配置组及对应 {count} 个配置项")   

    def load_data(self):
        """
        加载数据
        """
        self._user_file_path.parent.mkdir(exist_ok=True, parents=True)
        self._full_file_path.parent.mkdir(exist_ok=True, parents=True)
        if not self._full_file_path.exists():
            logger.info(f"完整配置文件 {self._file}.yaml 不存在，开始自动生成")
            self.generate_default()
        self.load_full_data()
        if self._user_file_path.exists():
            self.load_user_data()
            self.save_full_data()
        else:
            logger.info(f"用户配置文件 {self._file}.yaml 不存在，开始自动生成")
            self.save_user_data()
            logger.info(f"用户配置文件 {self._file}.yaml 生成成功")
