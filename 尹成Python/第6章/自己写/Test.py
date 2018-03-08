# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description:

## 6.5

def xFunction(x, y):
    print(x + y)
    print(x)
    return

xFunction( y=10, x = 50)        ##使用关键字参数调用函数
xFunction(10, 50)               ##使用位置参数调用函数

###############注意：Python位置参数不能出现在任何关键字参数之后



## 6.8
def function1(n, m):
    function2(3,4)

def function2(n):
    if n > 0:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        return -1


## 6.9
'''

def main():
    print(min(5,6))

def min(n1, n2):
    smallest = n1
    if n2 < smallest:
        smallest = n2

main()
'''



## 6.10
'''
def main():
    print(min(min(5,6), (51,6)))

def min(n1,n2):
    smallest = n1
    if n2 < smallest:
        snallest = n2

main()


error:
    if n2 < smallest:
    TypeError: '<' not supported between instances of 'tuple' and 'NoneType'
'''
