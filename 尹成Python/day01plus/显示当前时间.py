# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 显示当前时间

import time
while True:
    seconds = time.time()
    second = int(seconds % 60)
    minute = int(seconds / 60 % 60)
    hour = int(seconds / 3600 % 24)
    hour += 8
    print(hour, minute, second)
