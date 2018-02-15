# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 绘制一个矩形

import turtle

coordinate = input("请输入矩形中心的坐标：")
coordinate_x = eval(coordinate.split(',')[0])
coordinate_y = eval(coordinate.split(',')[1])

length = eval(input("请输入矩形的长度："))
width = eval(input("请输入矩形的宽度："))

turtle.penup()
turtle.goto(coordinate_x - length / 2, coordinate_y - width / 2)
turtle.pendown()
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width)

turtle.done()






