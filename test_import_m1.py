import sys
import os
from test_import import test_import_m3

def printSelf():
    print "this is m1"


print "m1:",__name__, __package__
print "sys.modules,m1:",sys.modules
test_import_m3.printSelf()