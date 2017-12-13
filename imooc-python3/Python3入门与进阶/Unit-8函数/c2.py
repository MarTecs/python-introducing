#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 函数的使用，以及修改Python中默认的递归深度


## 使用sys模块修改默认的递归最大深度，这里修改为10000
import sys
sys.setrecursionlimit(100)



def add(x, y):
    result = x + y;
    return result;

print(add(3,4))


'''
def print(x):
    print(x);

当我们调用这个方法的时候，将会调用我们自己写的print函数，报出如下错误
  [Previous line repeated 995 more times]

'''


## python中一个函数返回多个值
