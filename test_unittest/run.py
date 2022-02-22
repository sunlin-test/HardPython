# coding=utf-8

'''测试用例执行方式
1. 以测试脚本为入口模块执行
   1)本地运行、命令行运行
2. 以非测试脚本为入口模块执行
    用suite对象封装测试用例
   1）直接定义一个suite对象，再addTest(具体测试方法)  -- addTest不能添加以数据驱动的测试方法？
   2) 用testLoader去加载指定目录下文件中的测试用例到一个suite中  unittest.defaultTestLoader.discover(指定文件)
   执行suite
   1) unittest.main(defaultTest='suite')
   2) 定义一个runner对象，runner.run(suite)


'''
import unittest
import test1
from HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    # 加载部分测试用例到suite 1
    suite = unittest.TestSuite()
    #suite.addTest(test1.SampleTest("test_asstring4"))

    # # 加载测试用例文件到suite 2
    # # 通过TestLoader加载指定目录下的文件中的测试用例到suite
    suite = unittest.defaultTestLoader.discover("./",'test1.py')
    #
    # # 运行用例1
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    #
    # # 运行用例2
    # # 找到__main__下的suite属性，赋值给TestProgram.test，然后运行TestProgram.runTests()
    # # 在test1.py中直接执行unittest.main()：将默认加载test1.py中的所有测试用例
    unittest.main(defaultTest='suite')

    # report_file = open("HtmlReport.html",'wb+')
    # runner2 = HTMLTestRunner(stream=report_file)
    # runner2.run(suite)


