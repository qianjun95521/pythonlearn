import requests

class HtmlDownload(object):
    def download(self,url):
        headers = {
            'Referer': 'http://ggzyjy.jxsggzy.cn/hygs/huiyuaninfo/pages/shigonginfo/ShiGongInfo_Detail?DanWeiType=131&DanWeiGuid=8a817fab-4871-4201-b647-ea6ec0b05a03'
        }
        if url is None:
            return
        r=requests.get(url,timeout=10)
        if r.status_code==200:
            r.encoding=r.apparent_encoding
            return r.text
        return 