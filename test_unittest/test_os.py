# coding=utf-8

import os

name='AbcsF'
test_path = r'F:\sunlin-test\aest_unittest\aest_os.py'

# 将文件名都转为小写
name1 = os.path.normcase(name)
test_path1 = os.path.normcase(test_path)

print name1
print test_path1