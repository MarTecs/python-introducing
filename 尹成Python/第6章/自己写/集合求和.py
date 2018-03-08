# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 计算指定开始和结束的数之间所有数的集合


def sum(head, end):
    result = 0
    for i in range(head, end + 1):
        result += i
    return result

print(sum(1,10))