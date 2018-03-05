# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 金融应用程序，复利值


rate_year = 0.00417
money = eval(input("请输入你要存款的金额："))

for i in range(6):
    if i != 0:
        money = money + 100
    money = money * (1 + rate_year)
    print(money)

print("After the sixth month, the account value is %f" % money)
