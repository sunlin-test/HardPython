# coding=utf-8

import test_main

print "test_main2  __name__:",__name__

test_main.test_get_var()
print "test_main.test_var:",test_main.test_var
# print test_var  将报错

print isinstance("__main__",basestring)

# __name__ 模块导入，其变量、类、函数等都需通过模块名引用，否则为访问自己的,若自己没有，将报错。
# 变量、类、函数一定属于某一py文件，即属于某一模块。
# __name__等变量为模块的魔法变量，是每个模块都有的。指代模块名称。
# __name__==__main__，__main__特指入口文件/模块。


