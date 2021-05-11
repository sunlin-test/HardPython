#!/usr/bin/python
# -*- coding: utf8 -*-

print "Hello World!",
print "Hello Again",
print "I like typing this.",
print "This is fun.",
print "Yay! Printing.",
print "I'd match rather you 'not'.",
print 'I "said" do not match this.',
# python2默认以ASCII编码解析，总共128位，中文为在ASCII后新增的编码，ASCII无法识别
# 正则表达式 a+b a*b a?b +前面的一个字符a至少出现一次   *前面的一个字符a可出现任意次 ?前面的字符最多出现一次
# . 匹配除换行符\n外的任何单字符
# ^[abc] 不接受[]内的字符       [abc]匹配[]内的任意一个字符



print "你好，世界！",
print "你好，\n" \
      "世界"
