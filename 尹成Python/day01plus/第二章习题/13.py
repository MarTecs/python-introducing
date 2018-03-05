# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 分割数字

number = eval( input("Enter an integer：") )
print( number % 10 )
print( number // 10 % 10 )
print( number // 100 % 10 )
print( number // 1000 )
