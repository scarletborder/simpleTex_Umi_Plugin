# simpleTex Web API
**此插件仅供学习交流使用**  
plugin version: 0.1.0 适配于Umi-OCR v2.1.0  
使用[SimpleTex主页 致力于提供先进的公式识别/文档识别解决方案](https://simpletex.cn/ai/latex_ocr)的开放api文档提供的api接口，提供一个图片转为Tex文本的OCR方案  
![示例exapmple](example1-1.png)

## Dependence
新版本只需要requests即可
另外你需要开设一个[api服务器](https://github.com/scarletborder/SimpleTex-WebAPI)


## 关于置信度
如果识别类型（recognizing mode）为文档(document)或者自动(auto)时会出现不返回置信度的现象，属response不存在相关键值对的原因。