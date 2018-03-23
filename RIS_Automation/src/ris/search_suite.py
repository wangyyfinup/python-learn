##创建搜索模块的测试suite，生成自动化测试报告
import unittest
import HTMLTestRunner
import time,os,sys
if not "E:/eclipse/eclipse-workspace/ris_search_automation/RIS_Automation/src/ris/cases" in sys.path:
    sys.path.append("E:/eclipse/eclipse-workspace/ris_search_automation/RIS_Automation/src/ris/cases")
import  search_mohu,search_gaoji,search_selectByweixin,search_hotwords,search_selectBytimetype,search_selectByinfotype,search_selectBycross,search_selectByemotion

testunit=unittest.TestSuite()

#将测试用例添加到套件
testunit.addTest(unittest.makeSuite(search_mohu.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_gaoji.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_selectByweixin.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_hotwords.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_selectBytimetype.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_selectByinfotype.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_selectBycross.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_selectByemotion.UntitledTestCase))

#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#定义报告存放路径
now= time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
filename= "E:\\eclipse\\eclipse-workspace\\ris_search_automation\\RIS_Automation\\src\\ris\\report\\search-" + now + r'-report.html'

fp = open(filename,'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'信息搜索模块测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
        