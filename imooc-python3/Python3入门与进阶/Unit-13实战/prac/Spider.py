#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 自己写一个爬虫，用来爬取自己个人博客上的文章阅读量

import re
from urllib import request;

## 定义要爬虫的链接，这里由于自己博客链接只有6页所以，定义了6个链接
page_1 = "http://www.sivan0222.cn/";
page_2 = "http://www.sivan0222.cn/page/2/";
page_3 = "http://www.sivan0222.cn/page/3/";
page_4 = "http://www.sivan0222.cn/page/4/";
page_5 = "http://www.sivan0222.cn/page/5/";
page_6 = "http://www.sivan0222.cn/page/6/";


class Spider():

    ## 首先模拟一个Http链接
    http_connection = request.urlopen(page_1);
    htmls = http_connection.read();

    ## 获得标题的正则表达式
    title_pattern = "<>";

    ## 获得阅读量的表达式
    read_pattern = '<span class="leancloud-visitors-count"></span>';

    def __fetch_content(self,):
        htmls = Spider.http_connection.read();
        print(htmls)
        htmls = str(htmls, encoding="utf-8");
        print(htmls)
        print(re.findall(Spider.read_pattern, htmls));


    def go(self):
        self.__fetch_content();

s = Spider();
s.go();