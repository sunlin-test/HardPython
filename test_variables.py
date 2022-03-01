# coding=utf-8

class TestVariables(object):
    class_variable = 30

    def __init__(self):
        self.var = 10
        self.class_variable = 5

    def test_01(self):
        TestVariables.class_variable=20


test1 = TestVariables()
print test1.var
print test1.class_variable
test1.test_01()
print test1.class_variable
print TestVariables.class_variable