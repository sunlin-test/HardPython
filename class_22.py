# coding=utf-8


# def (define)定义函数  args=arguments参数
def print_two(*args):
    # 解包
    arg1, arg2 = args
    print "arg1: %r, arg2：%r" % (arg1, arg2)


def print_two_again(arg1, arg2):
    print "arg1: %r, arg2：%r" % (arg1, arg2)


def print_one(arg1):
    print "arg1: %r" % arg1


def print_non2():
    print "I'm got nothin'."

# 函数调用
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_non2()

