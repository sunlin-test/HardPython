# -*- coding: gbk -*-
from sys import argv
import time

filename = argv[1]
with open(filename, 'a+') as txt:
    print "��ǰλ�㣺%d" % txt.tell()
    print txt.read()

    print "��ǰλ�㣺%d" % txt.tell()
    txt.seek(0,2)

    str = 'this is add {}\n'.format(time.time())
    txt.write(str)
    txt.flush()

    print "��ǰλ�㣺%d" % txt.tell()
    txt.seek(0, 0)
    print "д����:",txt.read()


