# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 风寒湿度

temperature = eval(input("Enter the temperature between -58 and 41："))
speed_wind = eval(input("Enter the wind speed in miles per hour："))
chill_index = 35.74 + 0.6215 * temperature - 35.75 * (speed_wind ** 0.16) + 0.4275 * temperature * (speed_wind ** 0.16)
print("The wind chill index is %f" % chill_index)