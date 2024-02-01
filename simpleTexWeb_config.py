from plugin_i18n import Translator

# UI翻译
tr = Translator(__file__, "i18n.csv")

# 全局配置
globalOptions = {
    "title": "simpleTexWeb",
    "type": "group",
    "proxy_proto": {
        "title": "Proxies type",
        "optionsList": [["none", "no proxy"], ["http", "http"], ["https", "https"]],
        "toolTip": "proxies=http://* or https://* or not use proxy",
    },
    "proxy_addr": {
        "title": "proxy address",
        "default": "127.0.0.1:7890",
        "toolTip": "if you choose [no proxy] in [proxy_proto], this option is disable",
    },
    "api_key": {
        "title": "Api Key",
        "default": "web",
        "toolTip": "Fill your api key here, you can apply one in simpletex.cn. If you fill `web` here, plugin will try to call web api without an api_key",
    },
    "chromium_exe": {
        "title": "chromium path",
        "default": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "toolTip": "fill `chrome://version` in chrome or `edge://version` in edge to find the path",
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
        "toolTip": "this option is disable when `api_key` is not `web`",
    },
}
