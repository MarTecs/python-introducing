# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: round函数


## 1个参数的round函数：使用round函数进行取值，并不一定是四舍五入，当round函数中的数与两个整数的接近程度相同，那么将会返回偶数
num = 41.1
print(round(num))

## 2个参数的round函数：将会保留小数点后几位(由第2个参数指定)
num = 49.35955
print(round(num,4))

