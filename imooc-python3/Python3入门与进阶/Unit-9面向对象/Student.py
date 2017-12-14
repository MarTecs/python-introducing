#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 面向对象
class Student():
    name = '';
    age = 0;

    '''
    如果按照下面这样写类中的方法将会报错，因为类中的方法必须传入一个参数也就是self
    def print_file():
        print("name：" + name);
        print("age：" + str(age));
    '''
    '''
    如果按照下面这样写，将会报错name is undefined错误
    def print_file(self):
        print("name：" + name);
        print("age：" + age);
student = Student();
student.print_file();
    '''
    def print_file(self):
        print("name：" + self.name);
        print("age：" + str(self.age));

    ## 定义一个构造函数,Python要求构造函数只能返回None，如果返回其他就会报错
    def __init__(self):
        print("构造函数被调用了!");

student = Student();
student.print_file();

student2 = Student();
print(student2.__init__()); ##这样也可以调用构造函数，只是返回一个None