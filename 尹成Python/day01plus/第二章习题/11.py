# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 金融应用程序：投资额

final_value = eval(input("Enter final account value："))
interest_rate = eval(input("Enter annual interest rate in percent："))
number_years = eval(input("Enter number of years："))
print("Initial deposit value is %f" % ( final_value / ( ( 1 + interest_rate * 0.01 ) ** number_years ) ))