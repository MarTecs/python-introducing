#-*-coding:utf-8-*-
# Author: sivan
# computer: Deskttop
# description: 面向对象
class Student():

    ## 下面的name 和 age是类变量
    name = '';
    age = 0;

    ## 实例变量定义，必须是使用了self关键字
    ## 定义一个构造函数,Python要求构造函数只能返回None，如果返回其他就会报错
    def __init__(self, name, age):
        print("构造函数被调用了!");
        # name = name; ##Python会自动进行区分，但是只是自己进行赋值
        self.name = name;
        self.age = age;

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


'''
student = Student();
student.print_file();

'''

'''
测试Python的构造方法
student2 = Student();
print(student2.__init__()); ##这样也可以调用构造函数，只是返回一个None
'''

student2 = Student("吴晓文",18);
print(student2.age);
print(student2.name);
