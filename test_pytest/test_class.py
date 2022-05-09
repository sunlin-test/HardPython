# coding = utf-8

"""
1. 用例类，类名必须以Test开头
2. 用例类，不能有__init__方法，即不能继承自某个有__init__的类?
"""

import pytest

class TestClass(object):
    @pytest.mark.slow
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x,"check")

    def test_three(self):
        value = 9
        # 1.赋值一个ExceptionInfo对象给exec_info.
        # 2.raise抛出的异常信息(<class 'RuntimeError'>, RuntimeError('value must be <=10'), <traceback object at 0x0000021A2082FDC0>)，将被赋值给exec_info._exc_info
        # 3.exec_info.type,实际为取exec_info._exc_info[0]，即exec_type: <class 'RuntimeError'>
        with pytest.raises(RuntimeError) as exc_info:
            print(exc_info)
            if value > 10:
                raise RuntimeError("value must be <=10")

        assert exc_info.type is RuntimeError