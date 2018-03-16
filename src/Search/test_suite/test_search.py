##创建搜索模块的测试suite，生成自动化测试报告
import unittest
#import test_case.fuzzy_search as fuzzy_search,test_case.highlevel_search as highlevel_search
import HTMLTestRunner
import time,os,sys
if not "E:/eclipse/eclipse-workspace/ris_search_automation/RIS_Automation/src/Search/test_case" in sys.path:
    sys.path.append("E:/eclipse/eclipse-workspace/ris_search_automation/RIS_Automation/src/Search/test_case")
import  fuzzy_search,highlevel_search,hotwords,fuzzy_search_condition,highlevel_search_condition

testunit=unittest.TestSuite()

#将测试用例添加到套件
testunit.addTest(unittest.makeSuite(fuzzy_search.UntitledTestCase))
testunit.addTest(unittest.makeSuite(highlevel_search.UntitledTestCase))
testunit.addTest(unittest.makeSuite(hotwords.UntitledTestCase))
testunit.addTest(unittest.makeSuite(fuzzy_search_condition.UntitledTestCase))
testunit.addTest(unittest.makeSuite(highlevel_search_condition.UntitledTestCase))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#定义报告存放路径
now= time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
filename= "E:\\eclipse\\eclipse-workspace\\ris_search_automation\\RIS_Automation\\src\Search\\report\\" + now + r'-report.html'

fp = open(filename,'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'信息搜索模块测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
        