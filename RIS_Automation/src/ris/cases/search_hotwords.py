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
        u'''热搜词测试'''
        driver = self.driver
        
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
        #点击导航栏，进入信息搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        time.sleep(10)
        #验证10个热搜词是否都存在
        for i in range(1,5):
            driver.find_element_by_xpath("//*[@id='searchApp']/div[2]/div[1]/div["+str(i)+"]").is_displayed()
        for j in range(1,7):
            driver.find_element_by_xpath("//*[@id='searchApp']/div[2]/div[2]/div["+str(j)+"]").is_displayed()
        #点击最后一个热搜词
        driver.find_element_by_xpath("//div[@id='searchApp']/div[2]/div[2]/div[6]/span").click()
        time.sleep(2)
        #验证是否跳转到了百度页面
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to_window(handle)
        bdtitle=driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/a/img").get_attribute("title")
        print(bdtitle)
        assert bdtitle == "到百度首页"
        bdbutton=driver.find_element_by_xpath("//*[@id='su']").get_attribute("value")
        print(bdbutton)
        assert bdbutton=="百度一下"
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
