# coding=utf-8

"""装饰器的用法"""
from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print"I am doing some boring work before excuting a_func()"

        a_func()

        print "I am doing some boring work after excuting a_func()"

    return wrapTheFunction


# 定义一个想要被装饰的函数
def a_function_requiring_decoration():
    print "I am the function which need some decoration to move my foul smell"


# 未被装饰时执行函数
a_function_requiring_decoration()

# 装饰函数并赋值给原函数名，实际a_function_requiring_decoration()已为钮祜禄氏函数wrapTheFunction()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()


# 通过@装饰函数
@a_new_decorator
def a_function_requiring_decoration2():
    print "I am the function which need some decoration to move my foul smell2"


a_function_requiring_decoration2()
print a_function_requiring_decoration2.__name__