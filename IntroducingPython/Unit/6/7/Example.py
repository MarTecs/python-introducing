# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: self的自辩

class Car():
    def exclaim(self):
        print("I'm a Car")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish")
    def need_a_push(self):
        print("A little help here?")

car = Car()
car.exclaim()               ##这个是把car对象传递给exclaim()中的self参数，等同于如下代码！
Car.exclaim(car)

