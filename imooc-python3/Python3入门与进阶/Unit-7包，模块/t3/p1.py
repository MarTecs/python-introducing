#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 避免循环引入，p1引入p2,此时将会执行p2，但是p2中又引入p1，将会造成一个死循环


from p2 import p2
p1 = "a";
print(p2);