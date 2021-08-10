import sys
from . import test_import_m4



def printSelf():
    print "this is m3"


test_import_m4.printSelf()

print "m3:",__name__, __package__
print "sys.modules,m3:",sys.modules