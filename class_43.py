# coding=gbk
import sys
import socket
import uuid

stream = sys.stdout

print dir(stream)
print "encoding:",stream.encoding

hostname = socket.gethostname()
print socket.gethostbyname(hostname)
print uuid.uuid1(uuid.getnode())


class MyClass(object):

    def test1(self):
        print "this is def test1"

    def test2(self):
        print "this is def test2"

    def printSelf(self):
        print 'type1:', type(self)


myclass = MyClass()
print "myclass.__module__:",myclass.__module__
print getattr(myclass,'test2')()


test = lambda x:x * x
print test(5)

def build(x,y):
    return lambda:x * x + y * y

f = build(1,2)
print f()

f1 = lambda x:'test2' * x
print f1(2)

print sys.path


print None == ''
print None == []
print type(None)

test = None
if test:
    print "test is not None"
else:
    print "test is None"

L = []

L = [i ** 2 for i in range(1,11)]
print L

attrs = {"key1": "value1","key2": "value2","key3": "value3","key4": "value4"}
if "key1" in attrs:
    print "key1:",attrs.pop("key1")

print isinstance(1,int)

print sys.modules["__main__"]

print attrs.items()