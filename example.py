import requests

headers = {
            'Referer': 'http://ggzyjy.jxsggzy.cn/hygs/huiyuaninfo/pages/FrameAll?DanWeiType=131&DanWeiGuid=8a817fab-4871-4201-b647-ea6ec0b05a03'
        }
url="http://ggzyjy.jxsggzy.cn/hygs/huiyuaninfo/pages/shigonginfo/jxpShiGongInfoDetailForWebAction.action?cmd=page_Load&DanWeiType=131&DanWeiGuid=8a817fab-4871-4201-b647-ea6ec0b05a03&isCommondto=true"
r=requests.get(url,10)
if r.status_code==200:
    print(r.apparent_encoding)
    #r.encoding="ISO-8859-1"

    print(r.text)