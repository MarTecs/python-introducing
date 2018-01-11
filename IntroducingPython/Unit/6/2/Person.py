# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用Class定义类
class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    ##覆盖方法
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")

    def need_a_push(self):
        print("A little help here?")

car = Car()
car.exclaim()
yugo = Yugo()
yugo.exclaim()


## 开始写一个Person类
class Person():
    def __init__(self,name):
        self.name = name

class MDPerson():
    def __init__(self, name):
        self.name = "Doctor" + name

class JDPerson():
    def __init__(self, name):
        self.name = name + ',Esquire'




person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
print(doctor.name)
print(lawyer.name)


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_yugo.need_a_push()




