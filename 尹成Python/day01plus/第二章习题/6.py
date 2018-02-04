# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 对一个整数中的各位数字求和

number = eval(input("Enter a number between 0 and 1000："))
print("The sum of the digits is %d" % (number//100 + number % 10 + number // 10 % 10))