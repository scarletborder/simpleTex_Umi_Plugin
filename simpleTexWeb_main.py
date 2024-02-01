import random

# import io
import base64
import requests
import json
import time


class Api:  # 接口
    def __init__(self, globalArgd):
        if globalArgd["proxy_proto"] == "none":
            self.proxies = {}
        elif globalArgd["proxy_proto"] == "http":
            self.proxies = {"https": "http://" + globalArgd["proxy_addr"]}
        elif globalArgd["proxy_addr"] == "https":
            self.proxies = {"https": "https://" + globalArgd["proxy_addr"]}

        self.api_key = globalArgd["api_key"]
        self.chrome = globalArgd["chromium_exe"]
        self.timeout = globalArgd["timeout"]

        self.headers = {}
        self.data = {}

        self.ocr_request = None
        self.exit_func_list = []

    # 启动引擎。返回： "" 成功，"[Error] xxx" 失败
    def start(self, argd):
        # some settings which will be used in requests
        if self.api_key == "web":
            self.headers = {
                "authority": "server.simpletex.cn",
                "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
                "origin": "https://simpletex.cn",
                "referer": "https://simpletex.cn/",
                "sec-ch-ua": "Not",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-platform": "Windows",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-site",
            }

            characters = "ABCDEFGHJKMNP9gqQRSToOLVvI1lWXYZabcdefhijkmnprstwxyz2345678"
            uuid_value = "".join(random.choice(characters) for _ in range(128))
            self.data = {"uuid": uuid_value, "rec_mode": argd["rec_mode"]}
        else:
            self.headers = {"token": self.api_key}

        # define _ocr() func
        if self.api_key == "web":
            # 启动无头浏览器
            try:
                from DrissionPage import ChromiumOptions, ChromiumPage
            except BaseException as e:
                # may raise error when leak of package
                return f"[Error] Can not import DrissionPage, this may caused because your environment loses this package, try to install it{str(e)}"

            co = ChromiumOptions()
            co.set_browser_path(self.chrome)
            co.incognito()  # 匿名模式
            co.headless()  # 无头模式

            try:  # 打开无头网页
                ServerPage = ChromiumPage(co)
            except BaseException as e:
                co.headless(False)  # 关闭无头模式，下次以有头模式运行
                return f"[Error] Can not launch headless chromium page, may be you havn't specify chromium driver, find help in https://g1879.gitee.io/drissionpagedocs/get_start/before_start {str(e)}"

            try:
                ServerPage.get("./plugins/simpleTexWeb/latex_ocr.html")  #
            except BaseException as e:
                co.headless(False)  # 关闭无头模式，下次以有头模式运行
                return f"[Error] Can not open html file, is `latex_ocr.html` exists? {str(e)}"

            ServerPage.set.load_mode.none()

            def _ocr_request(file, FileType: str):
                characters = (
                    "ABCDEFGHJKMNP9gqQRSToOLVvI1lWXYZabcdefhijkmnprstwxyz2345678"
                )
                uuid_value = "".join(random.choice(characters) for _ in range(128))
                self.data["uuid"] = uuid_value

                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()} 加载文件{file[:16]} type {FileType}")

                # 无脑上image/jpeg了
                if FileType == "FilePath":
                    with open(file, "rb") as fin:
                        files = {"file": fin}
                        # get url
                        url = ServerPage.run_js_loaded(
                            "get_request_url('simpletex_ocr_v2_web')", as_expr=True
                        )
                        resp = requests.post(
                            url,
                            files=files,
                            data=self.data,
                            headers=self.headers,
                            proxies=self.proxies,
                            timeout=self.timeout,
                        )
                else:
                    if FileType == "base64":
                        binBytes = base64.b64decode(file)
                    elif FileType == "bytes":
                        binBytes = file

                    # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                    #     fout.write(f"\n {time.ctime()} 请求地址")
                    url = ServerPage.run_js_loaded(
                        "get_request_url('simpletex_ocr_v2_web')",
                        as_expr=True,
                    )
                    # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                    #     fout.write(f"\n {time.ctime()} 请求地址成功 {url}")
                    files = {"file": ("screenshot.png", binBytes, "image/png")}
                    # get url
                    # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                    #     fout.write(f"\n {time.ctime()}准备请求 {self.proxies}")
                    resp = requests.post(
                        url,
                        files=files,
                        data=self.data,
                        headers=self.headers,
                        proxies=self.proxies,
                        timeout=self.timeout,
                    )
                    # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                    #     fout.write(f"\n {time.ctime()} 请求结果 {resp.text}")

                if resp.status_code != 200:
                    return {"code": 102, "data": f"request failed - {resp.text}"}

                result = ServerPage.run_js_loaded(
                    f"get_parsed_result('{resp.text}')", as_expr=True
                )
                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()} 输出结果 {result}")

                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()} 开始解析json")
                result = json.loads(result)
                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()} json解析完成 {result}")
                if result["status"] is False:
                    return {
                        "code": 103,
                        "data": f"failed when local pharsing response from remote|| type:{str(FileType)} || encrypted code: {str(resp.text)} ||status: {str(result)}",
                    }

                result = result["res"]
                # 尝试得到confident
                confident = result.get("conf", 1)

                # 尝试得到markdown
                mdText = result.get("info", None)
                if isinstance(mdText, dict) is True:
                    mdText = result["info"].get("markdown", "")

                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()} 输出回主程序{mdText}")
                return {
                    "code": 100,
                    "data": [
                        {
                            "text": mdText,
                            "box": [[0, 0], [0, 0], [0, 0], [0, 0]],
                            "score": confident,
                        }
                    ],
                }

            def _page_when_exit():
                # 关闭无头浏览器进程并恢复配置
                # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
                #     fout.write(f"\n {time.ctime()}关闭无头浏览器")
                ServerPage.quit()
                co.headless(False)  # 关闭无头模式，下次以有头模式运行
                return

            self.ocr_request = _ocr_request
            self.exit_func_list.append(_page_when_exit)

        else:  # api_key

            def _ocr_request(file, FileType: str):
                url = r"https://server.simpletex.cn/api/latex_ocr"

                if FileType == "FilePath":
                    with open(file, "rb") as fin:
                        files = {"file": fin}
                        # get url
                        resp = requests.post(
                            url,
                            files=files,
                            data=self.data,
                            headers=self.headers,
                            proxies=self.proxies,
                            timeout=self.timeout,
                        )
                else:
                    if FileType == "base64":
                        binBytes = base64.b64decode(file)
                    elif FileType == "bytes":
                        binBytes = file
                    files = {"file": ("screenshot.png", binBytes, "image/png")}
                    resp = requests.post(
                        url,
                        files=files,
                        data=self.data,
                        headers=self.headers,
                        proxies=self.proxies,
                        timeout=self.timeout,
                    )

                if resp.status_code != 200:
                    return {"code": 102, "data": f"request failed - {resp.text}"}

                result = json.loads(resp.text)
                if result["status"] is False:
                    return {
                        "code": 103,
                        "data": f"failed when local pharsing response from remote - {str(result)}",
                    }

                confident = result["res"]["conf"]
                mdText = result["res"]["latex"]
                return {
                    "code": 100,
                    "data": [
                        {
                            "text": mdText,
                            "box": [[0, 0], [0, 0], [0, 0], [0, 0]],
                            "score": confident,
                        }
                    ],
                }

            self.ocr_request = _ocr_request
        return ""

    def stop(self):  # 停止引擎
        for func in self.exit_func_list:
            func()
        pass

    def runPath(self, imgPath: str):  # 路径识图
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} 路径视图")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imgPath, "FilePath")
        return res

    def runBytes(self, imageBytes):  # 字节流
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} 字节流")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imageBytes, "bytes")
        return res

    def runBase64(self, imageBase64):  # base64字符串
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} base64")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imageBase64, "base64")
        return res
