# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用Super从父类中获得帮助！

class Person():
    def __init__(self, name):
        self.name = name

class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email

print(EmailPerson('Bob Frapples', 'bob@frapples.com'))



