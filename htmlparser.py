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
        new_page_url_root="http://ggzyjy.jxsggzy.cn/hygs/huiyuaninfo/pages/shigonginfo/jxpShiGongInfoDetailForWebAction.action?cmd=page_Load&DanWeiType=131&DanWeiGuid="
        new_page_url_root2="&isCommondto=true"
        new_urls=[]
        if match.search(page_url) is not None:
            txt=soup.text.replace("\\", "")
            txt2=re.search(r'\"{.*}\"',txt).group(0).strip('\"')
            json_dict=json.loads(txt2)
            l_list=self._trans_json(json_dict)
            for l in l_list:
                new_urls.append(new_page_url_root+l+new_page_url_root2)
        return new_urls



    def _get_new_data(self,page_url,soup):
        match = re.compile(r".*/getTradeList\?response=application/json.*")
        if match.search(page_url) is not None:
            return
        print(soup.find("span",id="licencenum").string)

    def _trans_json(self,json_dict):
        q_list=json_dict.get("Table")
        r_list=[]
        for fac in q_list:
            r_list.append(fac.get("alink"))
        return r_list