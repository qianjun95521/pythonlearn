import re
from bs4 import BeautifulSoup
import json

class HtmlParser(object):
    def parser(self,page_url,page_content):
        if page_url is None or page_content is None:
            return
        soup=BeautifulSoup(page_content,"html.parser")
        new_urls=self._get_new_urls(page_url,soup)
        new_data=self._get_new_data(page_url,soup)
        return new_urls,new_data

    def _get_new_urls(self,page_url,soup):
        match=re.compile(r".*/getTradeList\?response=application/json.*")
        if match.search(page_url) is not None:
            json.load(soup)


    def _get_new_data(self,page_url,soup):