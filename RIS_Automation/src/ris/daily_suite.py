#coding=Utf-8
##创建日常监测模块的测试suite，生成自动化测试报告
import unittest
import HTMLTestRunner
import time,sys,os
pwd=os.getcwd()
if not pwd+"\cases" in sys.path:
    sys.path.append(pwd+"\cases")
import  daily_creategroup,daily_createtask,daily_turnpage,daily_selectinfo,daily_listoperation,daily_propagatepath,daily_duplicatecheck,index_addpicture,daily_similarmerge
testunit=unittest.TestSuite()
#将测试用例添加到套件
testunit.addTest(unittest.makeSuite(daily_creategroup.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_createtask.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_turnpage.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_selectinfo.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_listoperation.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_propagatepath.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_duplicatecheck.UntitledTestCase))
testunit.addTest(unittest.makeSuite(index_addpicture.UntitledTestCase))
testunit.addTest(unittest.makeSuite(daily_similarmerge.UntitledTestCase))
#定义报告存放路径
now= time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
filename= pwd+r'\report\daily-' + now + r'-report.html'
fp = open(filename,'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'日常监测模块测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)