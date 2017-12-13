#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 自定义一个返回绝对值的函数

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')     ##抛出一个错误
    if x < 0:
        return -x;
    else:
        return x;

print(my_abs(-85))
print(my_abs("s"))