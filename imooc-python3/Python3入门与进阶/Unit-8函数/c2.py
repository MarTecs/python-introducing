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


## python中一个函数返回多个值，将会以元祖的形式进行返回，但是不建议这样使用
def para(para1, para2):
    return para1, para2;

print(type(para(1,2))); #将会是一个元祖

result = para(1,2);
print(result[0], result[1]);    ##不建议这样获得结果值
dama1 , dama2 = para(1,2);      ##建议这样获得结果值，变量名更加有意义(相对使用序号来说)
print(dama1, dama2)

## 多

