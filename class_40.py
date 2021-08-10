# coding=utf-8
import six

# type是所有类的元类:类的类，用元类创建的是类，而非实例
a = 1
print a.__class__
print a.__class__.__class__
print a.__class__.__class__.__class__

'''定义类Hello2，类似于：
class Hello2:
    pass'''
Hello = type("Hello2",(),{})
hello = Hello()
print type(hello)


"""参数: 类名、父类(元组)、定义方法、属性(字典)
调用方法时，使用别名
创建实例时，使用类别名创建"""


def type_function(self):
    print "this is a function in type"


Hello3 = type("Hello4", (object,), {"type_function2":type_function,"name": "sunlin"})
hello3 = Hello3()
hello3.type_function2()
print hello3.name
print hello3.__class__


# __new__是python的构造方法,返回对象
# __init__是初始化方法
class MyClass(object):
    def __new__(cls, *args, **kwargs):
        print "this is a __new__ method"
        return object().__new__(cls)

    def __init__(self):
        print "this is a __init__ method"


myclass = MyClass()


# 自己定义元类
# 创建类时指定元类，即指定类的__new__采用元类的__new__进行创建,可在自定义元类中，通过修改attr对类添加类属性、类方法
class MetaClassMy(type):
    def __new__(cls, name, bases, attr):
        print "this is MetaClassMy's __new__"
        print name,bases,dict
        print "__module__:", attr["__module__"]
        attr["info"] = "metaclass info"
        attr["add"] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attr)



@six.add_metaclass(MetaClassMy)
class MyClass2(object):
    # def __new__(cls):
    #     print "this is MyClass2's __new__"
    pass

myclass2 = MyClass2()
print myclass2.info
myclass2.add(3)
