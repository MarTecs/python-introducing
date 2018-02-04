# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 将摄氏温度转化为华氏温度



degree_Celsius = eval(input("Enter a degree in Celsius："))

fahrenheit = ( 9 / 5 ) * degree_Celsius + 32
print("%d Celsius is %.1f Fahrenheit" % (degree_Celsius, fahrenheit) )

