import sys
from test_import_2 import test_import_m5


def printSelf():
    print "this is m4"

test_import_m5.printSelf()
print "sys.modules,m4:",sys.modules