# -*- coding: utf-8 -*-
#引入webdriver和unittest所需要的包
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

#引入HTMLTestRunner包
import HTMLTestRunner   

class Baidu(unittest.TestCase):
    #初始化设置
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #百度搜索用例
    def test_baidu(self):
        u'''百度搜索测试'''
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id("kw").click()
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium Webdriver")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     #定义一个单元测试容器
    testunit = unittest.TestSuite()
    #将测试用例加入到测试容器中
    testunit.addTest(Baidu("test_baidu"))
    #定义报告存放路径
    filename = r'E:\git\python-learn\src\report\result1.html'
    fp = open(filename,'wb')
    #定义测试报告
    runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'测试用例执行情况')
    
    #运行测试用例
    runner.run(testunit)
