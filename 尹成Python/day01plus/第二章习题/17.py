# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 健康应用程序：计算BMI


weight = eval(input("Enter weight in pounds："))
height = eval(input("Enter height in inches："))

BMI = weight * 0.45359237 / (( height * 0.0254 ) ** 2 )
print("BMI is %f" % BMI)
