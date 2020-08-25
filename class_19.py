# coding=utf-8

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %r to %r" % (from_file, to_file)

input = open(from_file)
indata = input.read()

# 计算文件内容长度
print "The input file is %d bytes long." % len(indata)

# exists() 文件是否存在
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit return to continue, hit CRTL-C to abort."

raw_input()

# 将从源文件中读取的内容写入目标文件
output = open(to_file, 'w')
output.write(indata)

print "Alright, all done."

output.close()
input.close()
