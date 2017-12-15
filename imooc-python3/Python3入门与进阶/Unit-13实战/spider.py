#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description:

import re
from urllib import request;

class Spider():

    url = "https://www.panda.tv/cate/yzdr"

    ## Python正则表达式中默认是贪婪的
    ## 老师问题：为什么这里不可以使用.替代[\s\S]
    root_pattern = '<div class="video-info">([\s\S]*?)</div>'
    name_pattern = '</i>([\s\S]*?)</span>';
    number_pattern = '<span class="video-number">([\s\S]*?)</span>';




    ##定义一个私有方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url);

        ## 此时读取到的是bytes的字节码，我们需要对其进行转换为字符串
        htmls = r.read();
        htmls = str(htmls, encoding="utf-8");
        return htmls;

    ## 分别返回姓名和人数
    def go(self):

        root_html = self.__analysis(self.__fetch_content());
        name_html = self.__name_analysis(root_html);
        number_html = self.__number_analysis(root_html);
        return name_html, number_html;

    def __analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls);
        return root_html[0];

    def __number_analysis(self, root_html):
        number_html = re.findall(self.number_pattern, root_html);
        return number_html;

    def __name_analysis(self, root_html):
        name_html = re.findall(self.name_pattern, root_html);
        return name_html;

s = Spider();
for i in range(2):
    print(s.go()[i]);

