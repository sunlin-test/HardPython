# coding=utf-8

'''unittest执行用例内部流程：
unittest.main() --TestProgram()的__init__()
                    参数解析self.parseArgs(argv) --根据参数找到脚本文件-测试类-测试方法(TestCase对象)，用TestSuite类的_tests多层包装
                                                再用self.test指向suite
                    运行测试脚本self.runTests()   --testRunner.run(self.test)
                                                    --suite.__call__ --指向suite的run方法
                                                                      --TestCase.__call__指向TestCase的run方法
                                                                        --TestCase.setUp()
                                                                        --TestCase.test_() / runTest()
                                                                        --TestCase.tearDown()
                                                  TextTestResult()记录case总数
'''

'''运行方式：
1. 命令行执行python -m unittest test1            --注：不能带.py   走loadTestsFromNames,test.py会被分为两部分，test1、py，test1中属性py不存在 报错
   入口非__name__==__main__，而是unittest包下的__main__.py   因为未收到传输argv，将采用sys.argv：python -m unittest test1
2. 命令行执行python test1.py                     --走loadTestsFromModule  ,module为入口模块,即test.py，查找模块下的测试类、测试方法
   不走-m时，在当前目录下查找，调用模块  执行入口__name__==__main__
3. 命令行执行python -m test1                     --走-m，模块名唯一时在任何目录下执行-m命令，通过sys.path自动查找模块名，通过-m调用该模块 如python -m pip
   执行入口模块的__name__==__main__
4. pycharm run执行test1.py
1）有多个用例时，光标放在某个用例，右键run 'Unittests' for test1.test_esstring3，则只执行这个用例  --pycharm的unittests插件功能
'''

'''unittest测试用例的4种执行结果 
1. 成功
2. 失败 --断言失败
3. 跳过 --unittest.skip()
4. 报错 --断言前抛异常
'''


import unittest
import sys


class SampleTest(unittest.TestCase):
    def test_esstring4(self):
        a = 'sdf'
        print "run test4"
        raise Exception

    def test_esstring3(self):
        a = 'sdf'
        print "run test3"
        self.assertEqual(isinstance(a, str), True)

    def test_asstring2(self):
        a = 'sdf'
        print "run test2"
        self.assertEqual(isinstance(a, int), True,"exception:True")

    @unittest.skip("skip")
    def test_asstring1(self):
        a = 'sdf'
        print "run test1"
        print "sys.path:", sys.path
        self.assertEqual(isinstance(a, str), True)

    # def runTest(self):
    #     # step1
    #     # a = 'sdf'
    #     # print "run test1"
    #     # self.assertEqual(isinstance(a, str), True,"error")
    #
    #     # step2
    #     a = 'sdf'
    #     #print "run test2"
    #     # diff_tool中调unicode(msg)，不能处理ascii编码，utf-8是ascii编码的一种
    #     # msg为英文时unicode(msg)可编码为type=unicode
    #     # msg为中文时需decode("utf-8")为unicode，否则unicode(msg)处理异常
    #     # msg = '不符合预期'.decode("utf-8")
    #     msg = "不符合预期"
    #     self.assertEqual(isinstance(a, str), False,msg)
    #
    #     # step3
    #     a = 'sdf'
    #     print "run test3"
    #     self.assertEqual(isinstance(a, str), False,"error")


if __name__ == "__main__":
    print "------------------start-------------------"

    # unittest.main()实际调用的是TestProgram()，即定义一个TestProgram对象，主要执行init()方法
    unittest.main()
    print "------------------end---------------------"

