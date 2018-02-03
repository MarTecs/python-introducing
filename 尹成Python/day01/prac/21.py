# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 显示时钟

import turtle


turtle.penup()
turtle.goto(0,-80)
turtle.pendown()
turtle.circle(80)


turtle.penup()
turtle.goto(0, -80)
turtle.pendown()
turtle.write("6")

turtle.penup()
turtle.goto(80, 0)
turtle.write("3")
turtle.pendown()

turtle.penup()
turtle.goto(0, 80)
turtle.write("12")
turtle.pendown()

turtle.penup()
turtle.goto(-80, 0)
turtle.write("9")
turtle.pendown()



turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(0,60)


turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.goto(60,0)


turtle.penup()
turtle.goto(0, -100)
turtle.write("9：15：00")
turtle.pendown()


turtle.penup()
turtle.goto(0, 0)
turtle.pendown()


turtle.done()