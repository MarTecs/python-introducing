# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用requests进行重写上面的例子


import requests
url = 'http://www.baidu.com'
resp = requests.get(url)


## 查看请求返回的结果类型
print(resp)

## 获取响应返回的状态码
print(resp.status_code)

## 获取响应内容
print(resp.text)


