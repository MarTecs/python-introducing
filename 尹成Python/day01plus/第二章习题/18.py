# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 当前时间

import time
strt = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(strt)
## 获得分割后的标准时间
time = strt.split(' ')[1].split(':')
## 输入时区偏差
time_offset = eval(input("Enter the time zone offset to GMT："))
hour = (int(time[0]) + time_offset + 24) % 24
minute = time[1]
seconds = time[2]
print(str(hour) + ":" + str(minute) + ":" + str(seconds))