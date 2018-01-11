# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用Python标准库来获取网站内容

import urllib.request as ur
url = 'http://www.baidu.com'
conn = ur.urlopen(url)
print(conn)
print(conn.status)
print(conn.getheader('Content-Type'))   ##Web服务器返回的数据格式


