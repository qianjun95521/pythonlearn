import urlmanager, htmldownload, htmlparser, dataoutput


class SpiderMan(object):
    def __init__(self):
        self.manager = urlmanager.UrlManager()
        self.download = htmldownload.HtmlDownload()
        self.dataoutput = dataoutput.DataOutput()
        self.parser = htmlparser.HtmlParser()

    def crawl(self, root_url):
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url() and self.manager.old_url_size() < 50:
            try:
                new_url = self.manager.get_new_url()
                html = self.download.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.dataoutput.saveFile(data)
            except Exception as e:
                print("crawl is failure!")

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl(
            "http://www.jxsggzy.cn/jxggzy/services/JyxxWebservice"
            "/getTradeList?response=application"
            "/json&pageIndex=1&pageSize=22&&dsname=ztb_data&bname=&qytype=4&itemvalue=181")
