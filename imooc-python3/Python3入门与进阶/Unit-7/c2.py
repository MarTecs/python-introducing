#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 视频教程上的列表，

fruits = [ ["apple", "grape", "banana"],(1,2,3,4)];
for i in fruits:
    for y in i:
        # print(y)  采用这种方式将会默认有一个换行！也就是等同于print(y,"\n");
        print(y,end="\t");

for i in fruits[1]:
    if i == 2:
        break;
    print(end="\n");
    print(i);


## 需要额外注意，当我们使用break终止循环的时候，else分支语句并不会执行！！！
for i in fruits[1]:
    if i == 2:
        break;
    print(i);
else:
    print("EOF");