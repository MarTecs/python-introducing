# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 咪西银行钱财(通过转分来实现)


money = eval(input("请输入转账的钱财："))
money = ( money * 10 - (int)(money * 10) ) / 10
print("米西了。", money)


