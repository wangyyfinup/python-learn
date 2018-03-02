import unittest
import ristest,baidutest
import HTMLTestRunner
import time,os

testunit=unittest.TestSuite()

#将测试用例添加到套件
testunit.addTest(unittest.makeSuite(ristest.UntitledTestCase))
testunit.addTest(unittest.makeSuite(baidutest.Baidu))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#定义报告存放路径
now= time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
filename= "E:\\git\\python-learn\\src\\test-suite\\" + now + r'-report.html'

fp = open(filename,'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'百度搜索测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
        