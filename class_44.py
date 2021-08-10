from class_43  import MyClass


class MyClass2(MyClass):
    def printSelf2(self):
        print "type2:", type(self)


myclass = MyClass2()
myclass.printSelf2()
myclass.printSelf()
