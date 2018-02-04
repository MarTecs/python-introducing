# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 财务应用程序：计算小费
subtotal, rate = eval(input("Enter the subtotal and gratuity rate："))
print(subtotal)
print(rate)
print("The gratuity is %f and the total is %f" % (subtotal * rate / 100, subtotal * rate / 100 + subtotal))




