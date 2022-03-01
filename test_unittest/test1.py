# coding=utf-8

'''unittest执行用例内部流程：
unittest.main() --TestProgram()的__init__()
                    参数解析self.parseArgs(argv) --testLoader根据参数找到脚本文件-测试类(loadTestsFromModule查找)-测试方法(getTestCaseNames查找-test开头且有__call__属性，若无则查找runTest()方法)(TestCase对象)，用TestSuite类的_tests多层包装
                                                再用self.test指向suite
                                                将一个测试类中的测试方法用一个suite封装，再用一个suite将多个测试类包装
                    运行测试脚本self.runTests()   --testRunner.run(self.test) (默认运行器TextTestRunner)
                                                    --suite.__call__ --指向suite的run方法
                                                                      --TestCase.__call__指向TestCase的run方法
                                                                        --setUpClass()  类前执行  --更适合环境前置条件及清理
                                                                        --TestCase.setUp() 在每个case执行前都调用一次
                                                                        --TestCase.test_() / runTest()
                                                                        --TestCase.tearDown() 在每个case执行后都调用一次
                                                                        --tearDownClass() 类后执行
                                                  默认TextTestResult()记录case总数
'''

'''运行方式：
1. 命令行执行python -m unittest test1            --注：不能带.py   走loadTestsFromNames,test.py会被分为两部分，test1、py，test1中属性py不存在 报错
   入口非__name__==__main__，而是unittest包下的__main__.py   因为未收到传输argv，将采用sys.argv：python -m unittest test1
   1)传输多个模块名 python -m unittest test1 test2
   2)传输模块下的测试类 python -m unittest test1.SampleTest
   3)传输具体测试用例 python -m unittest test1.SampleTest.test_asstring4
   4)传输某路径下某模块 python -m test_unittest.test1
2. 命令行执行python test1.py                     --走loadTestsFromModule  ,module为入口模块,即test.py，查找模块下的测试类、测试方法
   不走-m时，在当前目录下查找，调用模块  执行入口__name__==__main__
3. 命令行执行python -m test1                     --走-m，模块名唯一时在任何目录下执行-m命令，通过sys.path自动查找模块名，通过-m调用该模块 如python -m pip
   执行入口模块的__name__==__main__
4. pycharm run执行test1.py
1）有多个用例时，光标放在某个用例，右键run 'Unittests' for test1.test_esstring3，则只执行这个用例  --pycharm的unittests插件功能
'''

'''unittest测试用例的4种执行结果 
1. 成功 .     success = True --默认的result.addSuccess()未统计成功的case
2. 失败 E --断言失败          result.failures,case抛出failureException(具体test_用例执行过程中抛出)、_UnexpectedSuccess
3. 跳过 s --unittest.skip() result.skipped,case抛出SkipTest(具体test_用例执行过程中抛出)   --通过函数装饰器@unittest.skip()跳过，在test_用例执行时抛出。可在class、setup、某个case前跳过，setup、teardown不会运行
4. 报错 F--断言前抛异常       result.errors,case抛出其他异常
5. 预期报错 x --抛出用户自定义预期异常 result.expectedFailures
6. 非预期成功 u--抛出用户自定义预期异常result.unexpectedSuccesses 
'''

'''assertEqual()中msg传输中文异常问题 
python2默认是ascii码，中文通过repr()查看存储格式为\xe6\xa0\xa1\xe9\xaa  --十六进制。需将中文解码为unicode码制  msg.decode(encoding='utf-8')
diff_tool中调unicode(msg)，不能处理ascii编码，utf-8是ascii编码的一种
msg为英文时unicode(msg)可编码为type=unicode
msg为中文时需decode("utf-8")为unicode，否则unicode(msg)处理异常
1）diff_tool中在unicode(msg)前，添加代码msg = msg.decode(encoding='utf-8')  --可根本解决问题
2）测试用例传参msg前，msg = msg.decode(encoding='utf-8') --不能完全解决问题，抛出的异常中，msg为unicode代码，且过于冗余
'''

'''数据库驱动ddt
1. 在测试方法test_前添加装饰器@ddt.data(1,2,5,7)，以为测试用例增加测试数据func.DATA_ATTR=测试数据
2. 在测试类前添加装饰器@ddt.ddt，以拆分测试数据，创建并重命名多个测试方法set cls.test_asstring3_3_5(1)=test_asstring3(5)、set cls.test_asstring3_4_7(1)=test_asstring3(7)
   删除原有测试方法test_asstring3

3. 测试数据可以以文件形式传入@ddt.file_data()
4. 测试数据传入字典
    1)测试用例需设置接收参数**kwargvs，或指定变量名paramenter_version、mysql_version接收参数。@ddt.data({"mysql_version":'5.6',"paramenter_version":'test1'},
             {"mysql_version":'5.7',"paramenter_version":'test1'},
             {"mysql_version":'8.0',"paramenter_version":'test1'})
   2) @ddt.data(test_data)  --暂不知道如何处理,@unpack只会拆解一层？
   
'''

'''unittest.main() 传参含义
1.  module=__main__，入口模块，一般为测试用例所在模块
2.  defaultTest，默认执行的测试用例，为测试方法或suite
3.  verbosity 执行结果输出详细level
    =0 
    =1  . F S等省略信息
    >=2 OK  FAIL skip等详细信息
'''

'''封装夹具：多个测试用例重复的相同的代码封装到一个公共模块
问题1： 装饰器skip()不能使用
'''

from common.my_unit import MyUnit
import ddt
import sys

test_data = [{"mysql_version":'5.6',"paramenter_version":'test1'},
             {"mysql_version":'5.7',"paramenter_version":'test1'},
             {"mysql_version":'8.0',"paramenter_version":'test1'}]

@ddt.ddt
class SampleTest(MyUnit):
    # def test_esstring4(self):
    #     a = 'sdf'
    #     print "run test4"
    #     raise Exception
    #


    # @ddt.data(1,2,3,4)
    @ddt.data(test_data)
    @ddt.unpack
    def test_asstring3(self,paramenter_version,mysql_version):
        a = 'sdf'
        print "run test3"
        print mysql_version,paramenter_version
        # mysql_version2 = kwargs['mysql_version']
        # paramenter_version2 = kwargs['paramenter_version']
        # print mysql_version2,paramenter_version2
        #self.assertEqual(isinstance(a, str), False,'check error')

        #self.assertFalse(True,msg='校验失败')
        #
    # def test_asstring2(self):
    #     a = 'sdf'
    #     print "run test2"
    #     self.assertEqual(isinstance(a, int), True,"exception:True")

    # @MyUnit.skip
    def test_asstring4(self):
        a = 'sdf'
        print "run test4"
        msg = '校验失败'

        #msg = msg.decode(encoding='utf-8')
        # self.assertEqual(isinstance(a, str), False,'check error')
    # @unittest.skip("skip") 与 以下效果相同。将test_asstring()函数置换成skip_wrapper()
    # skip_test = unittest.skip("skip")
    # test_asstring4 = skip_test(test_asstring4)


    # def runTest(self):
    #     # step1
    #     # a = 'sdf'
    #     # print "run test1"
    #     # self.assertEqual(isinstance(a, str), True,"error")
    #
    #     # step2
    #     a = 'sdf'
    #     #print "run test2"

    #     # msg = '不符合预期'.decode("utf-8")
    #     msg = "不符合预期"
    #     self.assertEqual(isinstance(a, str), False,msg)
    #
    #     # step3
    #     a = 'sdf'
    #     print "run test3"
    #     self.assertEqual(isinstance(a, str), False,"error")




if __name__ == "__main__":
    print ord('a')
    print ord('c')
    print ord('e')
    print "------------------start-------------------"

    # unittest.main()实际调用的是TestProgram()，即定义一个TestProgram对象，主要执行init()方法
    MyUnit.main()
    print "------------------end---------------------"

