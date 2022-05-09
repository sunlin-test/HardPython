# coding = utf-8

"""
1. 用例类，类名必须以Test开头
2. 用例类，不能有__init__方法，即不能继承自某个有__init__的类?
"""


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")