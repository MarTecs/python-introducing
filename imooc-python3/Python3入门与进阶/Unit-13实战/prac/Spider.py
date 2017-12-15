#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 自己写一个爬虫，用来爬取自己个人博客上的文章阅读量


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
    http_connection = request.urlopen("page_1");
    htmls = http_connection.read();
