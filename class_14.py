# -*- coding: gbk -*-
from sys import argv
import time

filename = argv[1]
with open(filename, 'a+') as txt:
    print "当前位点：%d" % txt.tell()
    print txt.read()

    print "当前位点：%d" % txt.tell()
    txt.seek(0,2)

    str = 'this is add {}\n'.format(time.time())
    txt.write(str)
    txt.flush()

    print "当前位点：%d" % txt.tell()
    txt.seek(0, 0)
    print "写入后读:",txt.read()


