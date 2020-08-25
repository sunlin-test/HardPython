# coding=utf-8
# 导入sys中的argv模块，接收列表参数输入
from sys import argv

# 列表解包
script, filename = argv
# 打开一个文件，返回一个文件对象，类似定义一个文件对象       --python -m pydoc open
txt = open(filename)
# txt.read()，获取文件中的内容从头到尾，可read(10)取前几位数据，内容type为string
print "Here is your file %r:" % filename
print txt.read(10).decode('utf-8').encode('gbk')
# 控制台输入raw_input() 、 input()
print "Type the filename again:"
filename_again = raw_input("> ")

# 打开方式r+ 读写
txt_again = open(filename_again,'a+', )

# next()下一个值，已到EOF，则抛出异常
print "下一个值是:%s".decode('utf-8').encode('gbk') % txt.next()

# tell() 返回现在的位点
print "现在的文件位点是:%s".decode('utf-8').encode('gbk') % txt.tell()

# write()将内容写入缓冲区，缓冲区满自动写入文件
txt_again.write('this is add.')
# flush()将缓冲区内容立即写入文件
txt_again.flush()
# truncate()将位点后的文件内容删除
print txt_again.read().decode('utf-8').encode('gbk')
# txt_again.truncate()
print txt_again.readline()
print txt_again.readline()
# print txt_again.readlines()

print "%r文件状态为:%s".decode('utf-8').encode('gbk') % (filename, txt.closed)
# close()，先调flush()，再修改文件closed状态为true
txt.close()
print "%r文件关闭?%s".decode('utf-8').encode('gbk') % (filename, txt.closed)


