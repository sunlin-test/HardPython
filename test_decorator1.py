"""装饰器的原理：
在被装饰的函数执行前后做某些操作，将函数置换为被装饰过的函数"""

def hi(name = "sunlin"):
    print "now you are in the hi() function"

    def greet():
        return "now you are in the greet() function"

    def welcome():
        return "now you are in the welcome() function"

    if name == "sunlin":
        return greet
    else:
        return welcome


a = hi()
print a
print(a())
