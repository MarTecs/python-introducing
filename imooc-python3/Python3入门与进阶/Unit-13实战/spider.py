#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description:

import re
from urllib import request;

class Spider():

    url = "https://www.panda.tv/cate/yzdr"

    ## Python正则表达式中默认是贪婪的
    root_pattern = '<div class="video-info">[\s\S]*?</div>'


    ##定义一个私有方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url);

        ## 此时读取到的是bytes的字节码，我们需要对其进行转换为字符串
        htmls = r.read();
        htmls = str(htmls, encoding="utf-8");
        print(htmls)
        return htmls;

    def go(self):
        return s.__analysis(s.__fetch_content());

    def __analysis(self, htmls):
        root_html = re.findall(self.root_pattern, htmls);

        for i in len(root_html):
            print(i)


s = Spider();
s.go();

