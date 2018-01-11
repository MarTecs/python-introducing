# -*-coding:utf-8-*-
# Author: sivan
# computer: notebook
# description: 使用属性对特性进行访问和设置

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)

fowl = Duck('Howard')
fowl.set_name
print(fowl.name)
