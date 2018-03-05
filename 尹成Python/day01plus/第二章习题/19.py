# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 金融应用程序：计算未来投资额

investment_amount = eval(input("Enter investment amount："))
interest_rate = eval(input("Enter annual interest rate："))
number_years = eval(input("Enter number of years："))

accumulated_value = investment_amount * (1 + interest_rate * 0.01) ** number_years

print("Accumulated value is %f" % accumulated_value)
