# coding=utf-8


class MyClass(object):
    def __init__(self):
        self.name = 'MyClass'


class MyClass2:
    def __init__(self):
        self.name = 'MyClass2'


my_class = MyClass()
my_class2 = MyClass2()

print dir(my_class)
print my_class.__class__,my_class.__delattr__,my_class.__dict__
print dir(my_class2)