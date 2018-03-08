# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 求两个数中的大值

def max(number1, number2):
    if number1 > number2:
        return number1
    return number2

def main():
    i = 5
    j = 2
    k = max(i, j)
    print("The larger number of", i, "and", j, "is", k)

main()