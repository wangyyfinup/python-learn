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
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        u'''高级搜索筛选条件测试'''
        driver = self.driver
        driver.get("http://10.129.0.240:8083/login")
        driver.find_element_by_xpath("//input[@type='text']").send_keys("wangyanyan")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()

        driver.find_element_by_link_text(u"高级搜索").click()
        driver.find_element_by_xpath("//td[3]/label").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys(u"新华网")
        driver.find_element_by_xpath("//button[@type='button']").click()
        # 点击展开
        driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[5]/div[2]/div/div").click()
        #检查时间范围筛选条件是否都存在
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
        #检查信息类型筛选条件是否都存在
        info_condition=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[2]/div[1]/span").text
        assert info_condition == "信息类型："
        info_all=driver.find_element_by_id("info_all").text
        assert info_all == "全部"
        info_11=driver.find_element_by_id("info_11").text
        assert info_11 == "新闻"
        info_13=driver.find_element_by_id("info_13").text
        assert info_13 == "论坛"
        info_22=driver.find_element_by_id("info_22").text
        assert info_22 == "微博"
        info_21=driver.find_element_by_id("info_21").text
        assert info_21 == "微信"
        info_31=driver.find_element_by_id("info_31").text
        assert info_31 == "APP"
        info_12=driver.find_element_by_id("info_12").text
        assert info_12 == "平媒"
        info_41=driver.find_element_by_id("info_41").text
        assert info_41 == "境外"
        info_42=driver.find_element_by_id("info_42").text
        assert info_42 == "Twitter"
        info_43=driver.find_element_by_id("info_43").text
        assert info_43 == "Facebook"
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
        #信源分组筛选条件
        #driver.find_element_by_id("infoGroup_all").click()
        #driver.find_element_by_id("infoGroup_93").click()
        #driver.find_element_by_id("infoGroup_95").click()
        #driver.find_element_by_id("infoGroup_96").click()
        #driver.find_element_by_id("infoGroup_97").click()
        #收起筛选条件
        driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[5]/div/div/div").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
