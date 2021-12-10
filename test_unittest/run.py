# coding=utf-8

import unittest
from test_unittest.test1 import SampleTest
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    # 加载部分测试用例到suite 1
    suite = unittest.TestSuite()
    suite.addTest(SampleTest("test_esstring3"))

    # # 加载测试用例文件到suite 2
    # # 通过TestLoader加载指定目录下的文件中的测试用例到suite
    # suite = unittest.defaultTestLoader.discover("./",'test1.py')
    #
    # # 运行用例1
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #
    # # 运行用例2
    # # 找到__main__下的suite属性，赋值给TestProgram.test，然后运行TestProgram.runTests()
    # # 在test1.py中直接执行unittest.main()：将默认加载test1.py中的所有测试用例
    # unittest.main(defaultTest='suite')

    report_file = open("HtmlReport.html",'wb+')
    runner2 = HTMLTestRunner(stream=report_file)
    runner2.run(suite)


