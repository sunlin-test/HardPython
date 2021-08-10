# coding=utf-8

"""
复习函数和符号
"""

# with open("class_35.py") as f:
#     print f.read()
# print f.closed
class MyClass(object):
    def __init__(self):
        self.name = 'QA'
        print "this is __init__"

    def __exit__(self, type, value, trace):
        print "this is __exit__"
        print "type:", type
        print "value:", value
        print "trace:" ,trace


    def __enter__(self):
        print "this is __enter__"
        return self


with MyClass() as my_class:
    print type(my_class)
    print "name:", my_class.name
    print int(my_class.name)
    print "name2:", my_class.name

print "with 语句后"


