# coding=utf-8

"""装饰器类
将装饰功能封装，更加整洁"""
from functools import wraps
class logit(object):
    def __init__(self,logfile='out.log'):
        self.logfile = logfile

    def __call__(self, a_func):
        @wraps(a_func)
        def wrapfunction(*args,**kwargs):
            log_string = a_func.__name__ + 'was called'
            print log_string
            with open(self.logfile,'a') as log_file:
                log_file.write(log_string)
            self.notify()
            return a_func(*args,**kwargs)
        return wrapfunction

    def notify(self):
        print "this is notify"

@logit()
def myfunc1():
    print "this is myfunc1"

myfunc1()