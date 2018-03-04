# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 计算能量

M = eval(input("Enter the amount of water in kilograms："))
initialTemperatute = eval(input("Enter the initial temperature："))
finalTemperature = eval(input("Enter the final temperature："))
Q = M * (finalTemperature - initialTemperatute) * 4184
print("The energy needed is %.1f" % Q)

