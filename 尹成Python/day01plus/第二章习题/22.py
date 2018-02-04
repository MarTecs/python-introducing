# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 人口预测


year = int(input("请输入年数："))

seconds = year * 365 * 24 * 3600
people_number = 3120324986
birthPeople_number = seconds // 7
diePeople_number = seconds // 13
immigrantPeople_number = seconds // 45

futurePeople_number = people_number + birthPeople_number - diePeople_number + immigrantPeople_number
print("%d年后，人口预测为%d" % (year, futurePeople_number))







