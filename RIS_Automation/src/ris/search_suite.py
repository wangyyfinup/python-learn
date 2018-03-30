##创建搜索模块的测试suite，生成自动化测试报告
import unittest
import HTMLTestRunner
import time,sys,os
pwd=os.getcwd()
if not pwd+"\cases" in sys.path:
    sys.path.append(pwd+"\cases")
from cases import search_mohu,search_gaoji,search_selectByweixin,search_hotwords,search_selectBytimetype,\
search_selectByinfotype,search_selectBycross,search_selectByemotion,search_similarMerge,\
search_addmaterial,search_turnpage,search_addmonitor,search_addtrack,search_spreadpath

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
testunit.addTest(unittest.makeSuite(search_similarMerge.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_addmaterial.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_turnpage.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_addmonitor.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_addtrack.UntitledTestCase))
testunit.addTest(unittest.makeSuite(search_spreadpath.UntitledTestCase))
#执行测试套件
#runner = unittest.TextTestRunner()
#runner.run(testunit)

#定义报告存放路径
now= time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
#filename= "E:\\eclipse\\eclipse-workspace\\ris_search_automation\\RIS_Automation\\src\\ris\\report\\search-" + now + r'-report.html'
filename= pwd+r'\report\search-' + now + r'-report.html'

fp = open(filename,'wb')
runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'信息搜索模块测试报告',description=u'用例执行情况：')
#执行测试用例
runner.run(testunit)
        