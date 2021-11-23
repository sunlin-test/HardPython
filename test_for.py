# coding=utf-8

test_tuple = (1,2,3,4)

for element in test_tuple:
    print element


opts = ('-h', '--help')
for opt in opts:
    print "len(opt):",len(opt)
    print opt

test_tuple2 = ('a','b','c')
for element in test_tuple2:
    print element

new_opts = filter(None,('-h', '--help'))
print new_opts