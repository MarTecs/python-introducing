#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 视频教程上的列表，

fruits = [ ["apple", "grape", "banana"],(1,2,3,4)];
for i in fruits:
    for y in i:
        # print(y)  采用这种方式将会默认有一个换行！也就是等同于print(y,"\n");
        print(y,end="\t");