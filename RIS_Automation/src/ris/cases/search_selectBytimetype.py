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
        u'''按时间范围筛选测试'''
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
        #点击信息搜索，进入信息搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        
        #输入北京，进行模糊搜索
        driver.find_element_by_xpath("//*[@id='searchApp']/div[1]/div/form/div/div/div/div[1]/div/input").send_keys(u"北京")
        driver.find_element_by_css_selector("#searchApp > div.s_row.ivu-row > div > form > div > div > div > div.s-right > img").click()
        time.sleep(5)
        #验证时间范围筛选条件是否都存在
        time_condition=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[1]/span[1]").text
        assert  time_condition == "时间范围："
        time1=driver.find_element_by_id("date_1").text
        assert time1 == "最近一天"
        time2=driver.find_element_by_id("date_2").text
        assert time2 == "最近一周"
        time3=driver.find_element_by_id("date_3").text
        assert time3 == "最近一月"
        time4=driver.find_element_by_id("date_4").text
        assert time4 == "自定义"
        #获取信息列表中最近一天的信息数量
        list_num_day=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        
        #点击最近一周，获取最近一月的信息量
        driver.find_element_by_id("date_2").click()
        time.sleep(5)
        list_num_week=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        assert int(list_num_week) >= int(list_num_day)
        
        #点击最近一月，获取最近一月的信息量
        driver.find_element_by_id("date_3").click()
        time.sleep(5)
        list_num_month=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        assert int(list_num_month) >= int(list_num_week)
        
        #点击自定义，按照自定义时间筛选，自定义时间范围为当天00之后至下一天00点之前
        driver.find_element_by_id("date_4").click()        
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[1]/span[2]/div[1]/div[1]/div/input").send_keys(time.strftime('%Y-%m-%d 00:00',time.localtime(time.time())))
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[1]/span[2]/div[2]/div[1]/div/input").send_keys(time.strftime('%Y-%m-%d 24:59',time.localtime(time.time())))
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[1]/span[2]/button").click()
        time.sleep(5)
        list_num_custom=driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[6]/div[2]/div/div/span[2]").text
        assert int(list_num_custom)<= int(list_num_day)


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
