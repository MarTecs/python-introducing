# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 数据类型进行转换


num = 40
print(type(num))

num = 40.5
print(type(num))

num = int(num)
print(num)
print(type(num))

num = "40.5"
print(type(num))
##print(int(num)) ##将会报错，下面是正确的写法，int只是用来将实数转换为整数
print(int(eval(num)))