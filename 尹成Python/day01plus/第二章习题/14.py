# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 几何方面：三角形的面积

import math

points_triangle = eval(input("Enter three points for a triangle："))

x1 = points_triangle[0]
y1 = points_triangle[1]
x2 = points_triangle[2]
y2 = points_triangle[3]
x3 = points_triangle[4]
y3 = points_triangle[5]


## x1,x2
side1 = math.sqrt( (x1 - x2) ** 2 + (y1 - y2) ** 2 )

## x1,x3
side2 = math.sqrt( (x1 - x3) ** 2 + (y1 - y3) ** 2 )

## x2,x3
side3 = math.sqrt( (x2 - x3) ** 2 + (y2 - y3) ** 2 )

s = (side1 + side2 + side3) / 2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of triangle is %f" % area)