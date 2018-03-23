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
        u'''信息列表按情感类型筛选测试'''
        driver = self.driver
        #登录
        driver.get("http://10.129.0.240:8083/login")
        driver.find_element_by_xpath("//input[@type='text']").send_keys("wangyanyan")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        #验证导航栏内容
        navigation_list=['首页','日常监测','事件追踪','帐号监测','信息搜索','报告管理','境外帐号监测']
        for i in range(1,8):
            navigation_name=driver.find_element_by_xpath("//div[@id='sysHead_div']/li["+str(i)+"]").text
            assert navigation_name == navigation_list[i-1]
        #点击信息搜索，进入信息搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        
        #输入北京，进行模糊搜索
        driver.find_element_by_xpath("//*[@id='searchApp']/div[1]/div/form/div/div/div/div[1]/div/input").send_keys(u"北京")
        driver.find_element_by_css_selector("#searchApp > div.s_row.ivu-row > div > form > div > div > div > div.s-right > img").click()
        time.sleep(5)
        
        # 点击展开
        driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[5]/div[2]/div/div").click()
        
        #检查情感倾向筛选条件是否都在
        emotion_condition=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[4]/div[1]/span").text
        assert emotion_condition=="情感倾向："
        all_emotion=driver.find_element_by_id("emotion_2").text
        assert all_emotion=="全部"
        positive_emotion=driver.find_element_by_id("emotion_1").text
        assert positive_emotion=="倾向正面"
        negative_emotion=driver.find_element_by_id("emotion_-1").text
        assert negative_emotion=="倾向负面"
        medium_emotion=driver.find_element_by_id("emotion_0").text
        assert medium_emotion=="倾向中性"
        
        #获取信息列表中最近一天的全部情感类型的信息数量
        list_num_all=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        
        #点击倾向正面，获取列表信息量
        driver.find_element_by_id("emotion_1").click()
        time.sleep(5)
        list_num_positive=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
                
        #点击倾向负面，获取列表信息量
        driver.find_element_by_id("emotion_1").click()
        time.sleep(5)
        list_num_nagative=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        
        #点击倾向中性，获取列表信息量
        driver.find_element_by_id("emotion_0").click()        
        time.sleep(5)
        list_num_Medium=driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[6]/div[2]/div/div/span[2]").text
        
        print(list_num_all,list_num_Medium,list_num_nagative,list_num_positive)
        assert int(list_num_all)<= (int(list_num_positive)+int(list_num_nagative)+int(list_num_Medium))

        #收起筛选条件
        driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[5]/div/div/div").click()
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
