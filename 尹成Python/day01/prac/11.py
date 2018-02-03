# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 人口预测


time = 5 * 365 * 24 * 3600
people = 3120324986
birth = time // 7
die = time // 13
immigrant = time // 45

print("预测当前人口为：", people + birth - die + immigrant)