# coding=utf-8


def test_argv(argv1):
    print "数组：",argv1
    argv1.append('abc')
    print "数组2：",argv1


def test_argv2(argv1):
    print "数组：",argv1
    argv1["key2"] = "word2"
    print "数组2：",argv1


def test_argv3(argv1):
    print "数组：",argv1
    argv1 = argv1 * 2
    print "数组2：",argv1


list1 = [1,2]
test_argv(list1)
print "数组3：",list1

dict1 = {"key1": "word1"}
test_argv2(dict1)
print "数组3：",dict1

string1 = "teststring"
test_argv3(string1)
print "数组3：",string1

