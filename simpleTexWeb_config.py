from plugin_i18n import Translator

# UI翻译
tr = Translator(__file__, "i18n.csv")

# 全局配置
globalOptions = {
    "title": "simpleTexWeb",
    "type": "group",
    "host_addr": {
        "title": "host_addr",
        "default": "127.0.0.1:12933/upload/",
        "toolTip": "address of the deployed API server",
    },
    "token": {
        "title": "Authorization token to the deployed API server",
        "default": "web",
        "toolTip": "Fill your token here. Maybe empty if remote not set this",
    },
    "timeout": {
        "title": "timeout",
        "isInt": False,
        "default": 15.0,
        "unit": "seconds",
        "toolTip": "timeout of requests. A multi-lines formula sometimes consumes more than 6 secs",
    },
}

# 局部配置
localOptions = {
    "title": "simpleTexWeb",
    "type": "group",
    "rec_mode": {
        "title": tr("识别类型"),
        "optionsList": [
            ["formula", tr("公式")],
            ["document", tr("文档")],
            ["auto", tr("自动检测")],
        ],
        "toolTip": "rec mode",
    },
}
