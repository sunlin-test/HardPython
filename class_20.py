# coding=utf-8

from sys import argv
from os.path import exists
from os.path import getsize
import shutil
import os


script, from_file, to_file = argv

print "Copying from %r to %r" % (from_file, to_file)

# 计算文件内容长度
print "The input file is %d bytes long." % getsize(from_file)

raw_input()

# 将从源文件中读取的内容写入目标文件
shutil.copyfile(from_file, to_file)
# shutil.copy(from_file, './test')
# os.system('copy %s %s' % (from_file,to_file))
print "Alright, all done."



