# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 物理方面：计算跑道长度

speed, acceleration = eval(input("Enter speed and acceleration："))
print("The minimum runway length for this airplane is %.3f meters" % (speed * speed / ( 2 * acceleration )))
