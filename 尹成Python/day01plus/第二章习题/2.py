# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 计算圆柱体的体积

import math

number = input("Enter the radius and length of a cylinder：")
radius = eval(number.split(',')[0])
height = eval(number.split(',')[1])

print("The area is %f", math.pi * radius * radius)
print("The area is %f", math.pi * radius * radius)
print("The volume is %f", math.pi * radius * radius * height)
print("The volume is %f",math.pi * radius ** 2 * height)

