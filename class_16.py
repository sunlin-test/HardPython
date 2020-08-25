# coding=gbk

filename = 'class_15_sample.txt'
txt = open(filename)

print "中文"
# 对获取到的文件内容先按utf-8解码为unicode(二进制)，再按gbk编码
print "Here is your file %r:" % filename
print txt.read().decode("utf-8").encode("gbk")

print "Type the filename again:"
filename_again = raw_input("> ")

txt_again = open(filename_again)

print txt_again.read(12).decode("utf-8").encode("gbk")