# coding=utf-8

'''
1. 不用导pytest包
2. case方法以test_开头
3. 在cmd命令中执行pytest，自动扫描当前目录下的test_开头/_test结尾的文件并执行测试
4. 用例类，类名必须以Test开头
5. 用例类，不能有__init__方法，即不能继承自某个有__init__的类?
6. 调用pytest用例方法：
1) 在用例所在目录，cmd命令行执行:  pytest  --自动扫描当前目录下的test_开头/_test结尾的文件并执行测试。若文件中存在测试类，则查找以Test开头的类，继而查找类中的test_开头的case
2） 指定测试文件，cmd命令行执行:  pytest test_class.py
3)  指定测试目录，cmd命令行执行:  pytest test_pytest/    。可以扫描到子目录中的case
4)  指定case，cmd命令行执行:   pytest test_sample.py::test_answer   。没有测试类时指定case  --实际为指定唯一node id
                            pytest test_class.py::TestClass::test_one 。 有测试类时指定case
5)  指定标记case
6)  指定包，pytest --pyargs test_pytest
7)  python运行: python3 -m pytest test_class.py
'''

import pytest

def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5


def f():
    raise SystemExit(1)

def test_mytest():
    with pytest.raises(SystemExit):
        f()


