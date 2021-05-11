# coding=utf-8
print "I will now count my chickens:"
print "Hens", 25 + 30.0/6
print "Roosters", 100 - 25 * 3 % 4.0
print "Now I will count my eggs:"
# %取余   python2  /整数除且取整      python3 /除
print 3 + 2 + 1 -5 + 4 % 2 - 1 / 4 + 6
# python2 /一方有浮点数则作为浮点数运算保留小数
print "How about 1.0/4?",1.0/4
# python2 //除且取整
print "How about 1.0//4?",1.0//4
print "Is it true that 3 + 2 < 5 -7?"
# + - 优先级高于><
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3 + 2.0
print "What is 5 - 7", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
a = 1
b = 2
# python2 的print非函数，调用无需加()  print3的print为函数，调用方式print()
# python3 主打print() + 字符串函数formate()
print "a= %d,b = %d" % (a, b)
