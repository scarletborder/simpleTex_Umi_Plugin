from . import simpleTexWeb_main
from . import simpleTexWeb_config

PluginInfo = {
    "group": "ocr",  # 固定写法，定义插件组
    "global_options": simpleTexWeb_config.globalOptions,  # 全局配置字典
    "local_options": simpleTexWeb_config.localOptions,  # 局部配置字典
    "api_class": simpleTexWeb_main.Api,  # 接口类
}
