# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 绘制一个圆

import turtle

radius = eval(input("请输入圆的半径："))
coordinate_x = eval(input("请输入圆心的横坐标："))
coordinate_y = eval(input("请输入圆心的纵坐标："))

turtle.write("(0,0)")
turtle.penup()
turtle.goto(coordinate_x, coordinate_y - radius)
turtle.pendown()
turtle.circle(radius)


turtle.done()






