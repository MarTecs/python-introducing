# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 计算年数和天数

minutes = eval(input("Enter the number of minutes："))

years = minutes // ( 365 * 24 * 60)
days = minutes % ( 60 * 24 * 365 ) // ( 24 * 60 )
print("%d minutes is approximately %d years and %d days" % (minutes,years, days))