# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''高级搜索测试'''
        driver = self.driver
        #登录
        driver.get("http://10.129.0.240:8083/login")
        driver.find_element_by_xpath("//input[@type='text']").send_keys("zdhcs_02")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("1q2w3e4r5t%")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        #验证导航栏内容
        navigation_list=['首页','日常监测','事件追踪','帐号监测','信息搜索','报告管理','境外帐号监测']
        for i in range(1,8):
            navigation_name=driver.find_element_by_xpath("//div[@id='sysHead_div']/li["+str(i)+"]").text
            assert navigation_name == navigation_list[i-1]
        #点击导航栏，进入搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        #输入关键词等内容，进行高级
        driver.find_element_by_link_text(u"高级搜索").click()
        #包含全部关键词
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/form[1]/div[1]/div[2]/div/div/div[1]/textarea").send_keys("习近平 国家")
        #包含任意关键词
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/form[1]/div[2]/div[2]/div/div/div[1]/textarea").send_keys("人民 时代 会议")
        #排除词
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/form[1]/div[3]/div[2]/div/div/div[1]/textarea").send_keys("接见")
        #点击选择新闻信息类型
        driver.find_element_by_xpath("//td[1]/label").click()
        #输入新闻站点名称
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/div[2]/div/form[2]/div[1]/div[2]/div/div/div/input").send_keys(u"新华网")
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(10)
        #验证关键词生成的逻辑表达式 ，和相应个筛选条件都符合预期
        expressions=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[1]/div/div[1]//input").get_attribute("value")
        assert expressions==" ( 习近平 & 国家 )  &  ( 人民 | 时代 | 会议 )  &  (  ( !接见 )  ) "
        siteName=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[1]/div/div[2]//input").get_attribute("value")
        assert siteName=="新华网"
        #验证信息列表的数量大于0
        list_num=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        assert int(list_num) > 0
        img=driver.find_element_by_xpath("//*[@id='report']/table/tbody/tr[1]/div[2]/div[1]/img").get_attribute("src")
        assert img == "http://10.129.0.240:8083/static/img/news.4b644f3.png"
    

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
