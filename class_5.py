# -*- coding: utf-8 -*-

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary, do_not)
print(x)
print(y)
print("I said:%s" % x)
print("I also said:%s" % y)
hilarious = False
# %r、%s 字符串 %c单个字符 %d十进制整数 %f浮点数
joke_evaluation = "Isn't that joke so funny?!%r"
print(joke_evaluation % hilarious)
w = "This the left side of..."
x = "a string with a right side"
#字符串的连接运算
print(w + x)
