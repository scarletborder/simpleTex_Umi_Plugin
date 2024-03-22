# import io
import base64
import requests
import json


class Api:  # 接口
    def __init__(self, globalArgd):
        self.addr = globalArgd["host_addr"]
        self.timeout = globalArgd["timeout"]

        self.headers = {"Authorization": globalArgd["token"]}
        self.data = {}

    # 启动引擎。返回： "" 成功，"[Error] xxx" 失败
    def start(self, argd):
        # some settings which will be used in requests
        self.data = {"rec_mode": argd["rec_mode"]}
        return ""

    def stop(self):  # 停止引擎
        return

    def ocr_request(self, file, FileType: str):
        url = self.addr

        if FileType == "FilePath":
            with open(file, "rb") as fin:
                files = {"file": fin}
                # get url
                resp = requests.post(
                    url,
                    files=files,
                    data=self.data,
                    headers=self.headers,
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
                timeout=self.timeout,
            )

        if resp.status_code != 200:
            return {"code": 102, "data": f"request failed - {resp.text}"}

        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {resp.text} base64")
        result = json.loads(resp.text)
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {result}")

        if result["status"] is False:
            return {
                "code": 103,
                "data": f"failed when local pharsing response from remote - {str(result)}",
            }

        result = result["res"]
        rec_type = result["type"]

        confident = 1.0
        mdText = "NULL"
        if rec_type == "formula":
            confident = result["res"]["conf"]
            mdText = result["res"]["info"]
        elif rec_type == "doc":
            mdText = result["info"]["markdown"]
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {mdText} {confident} return")
        res = {
            "code": 100,
            "data": [
                {
                    "text": mdText,
                    "box": [[0, 0], [200, 0], [200, 40], [0, 40]],
                    "score": confident,
                }
            ],
        }
        return res

    def runPath(self, imgPath: str):  # 路径识图
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} 路径视图")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly1",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imgPath, "FilePath")
        return res

    def runBytes(self, imageBytes):  # 字节流
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} 字节流")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly2",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imageBytes, "bytes")
            # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
            #     fout.write(f"\n {res} return")
        return res

    def runBase64(self, imageBase64):  # base64字符串
        # with open("./plugins/simpleTexWeb/log.txt", "a") as fout:
        #     fout.write(f"\n {time.ctime()} base64")
        res = {
            "code": 104,  # 自定错误码：>101的数值
            "data": "[Error] Can not load plugin correctly3",
        }
        if self.ocr_request is not None:
            res = self.ocr_request(imageBase64, "base64")
        return res
