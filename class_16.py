# coding=gbk

filename = 'class_15_sample.txt'
txt = open(filename)

print "����"
# �Ի�ȡ�����ļ������Ȱ�utf-8����Ϊunicode(������)���ٰ�gbk����
print "Here is your file %r:" % filename
print txt.read().decode("utf-8").encode("gbk")

print "Type the filename again:"
filename_again = raw_input("> ")

txt_again = open(filename_again)

print txt_again.read(12).decode("utf-8").encode("gbk")