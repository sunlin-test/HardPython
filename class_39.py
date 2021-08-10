# coding=utf-8


i = raw_input("the frist: ")
j = raw_input("the second: ")

# assert i==j, "i!=j"

def assert_equel(current,expect,message):
    if current != expect:
        try:
            raise AssertionError,"预期:%s，实际值:%s,检查不通过,%s" % (current,expect,message)
        except AssertionError as e:
            print e.message
            return False
    return True


assert_equel(i,j,"i!=j")