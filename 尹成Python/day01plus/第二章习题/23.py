''# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 绘制四个圆

import turtle

radius = eval(input("请输入圆的半径："))

turtle.write("(0,0)")

turtle.penup()
turtle.goto(-radius, -2 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius, 0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, -2 * radius)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius, 0)
turtle.pendown()
turtle.circle(radius)

turtle.done()