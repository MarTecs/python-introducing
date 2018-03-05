# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 金融应用程序：计算利息

balance, interest_rate = eval(input("Enter balance and interest rate (e.g., 3 for 3%)："))
interest = balance * (interest_rate) / 1200
print("The interest is %f" % interest)