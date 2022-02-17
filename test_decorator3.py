# coding=utf-8

"""函数中嵌套装饰器"""
from functools import wraps


def logit(logfile = 'out.log'):
    def a_decorator(a_fun):
        @wraps(a_fun)
        def wrapfunction(*args,**kwargs):
            log_string = a_fun.__name__ + "was called"
            print log_string
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
            return a_fun(*args,**kwargs)
        return wrapfunction
    return a_decorator


@logit()
def myfunc1():
    pass

myfunc1()


@logit()
def myfun2(name):
    print name

myfun2("sunlin")