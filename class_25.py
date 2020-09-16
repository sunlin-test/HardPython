#coding=utf-8

from sys import argv
# 从sys导入argv至缓存
# script, filename = argv
# 对输入参数变量argv解包


def print_all(f):
# 定义函数，形参f，为file对象
    print f.read()
    # file.read()，读取并print当前位点后的所有内容


def rewind(f):
     f.seek(0)
     # 重新设置file的位点，0代表文件开头


def print_a_line(line_count, f):
    print line_count, f.readline()
    # 输出当前位点所在行，若当前位点在行尾，输出下一行

def print_remaining_lines(f):
    for i in f.readlines():
        # file.readlines()重复以file.readline()读取下一行信息，存储为list
        print i,


filename = 'class_25_sample.txt'
current_file = open(filename)

print "First, let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

print "Let's print the remaining lines:"
print_remaining_lines(current_file)

# add   iadd
current_line += 1
print "current_line = %s" % current_line

# iadd 可变对象，iadd传入两个参数，左边对象指向不变，即两个参数值均改变
current_list = [1,2,3]
b=[4]
second_list = current_list
current_list += b
print "current_list = %s,second_list = %s" % (current_list,second_list)
# add 可变对象，add传入两个参数，左边对象指向新对象，即左边参数改变，右边参数指向不变，值不变
current_list = [1,2,3]
b=[4]
second_list = current_list
current_list = current_list + b
print "current_list = %s,second_list = %s" % (current_list,second_list)




