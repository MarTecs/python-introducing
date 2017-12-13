#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: python中的参数类型

## 1. 必须参数
## 2. 关键字参数
## 3. 默认参数


## 使用关键字参数进行赋值
def add(x,y):
    return x + y;
print(add(y=3,x=5));


## 采用默认参数
def info(name, age="15", gender="女", address="怀仁县"):
    print("我叫" , name);
    print("我的年龄是", age);
    print("我的性别是", gender);
    print("我的地址是", address);

info("吴晓文","20","男","山西省");
print("下面采用默认参数".center(50,"-"))
info("sivan");
