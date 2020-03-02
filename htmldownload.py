import requests

class HtmlDownload(object):
    def download(self,url):
        if url is None:
            return
        r=requests.get(url)
        if r.status_code=200:
            r.encoding=r.apparent_encoding
            return r.text
        return 