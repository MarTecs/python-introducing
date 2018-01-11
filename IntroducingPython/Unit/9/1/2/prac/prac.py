# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用Python进行网络连接

from urllib import request

## 此时得到的re将会是一个响应对象
re = request.urlopen('http://www.baidu.com')


## 获取响应头的键值对：
if re.status == 200:
    for key, value in re.getheaders():
        print(key, value)

