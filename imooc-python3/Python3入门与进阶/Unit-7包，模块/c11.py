#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description:


##from t2 import c7
print("----")
from t2.c7 import a     ##即使当我们导入的只是包中一个模块的变量，也会执行__init__.py
print(a);
##import t2   ##当我们导入p2包的时候。将会默认执行__init__.py