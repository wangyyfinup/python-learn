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
        u'''高级搜索测试'''
        driver = self.driver
        driver.get("http://10.129.0.240:8083/login")

        driver.find_element_by_xpath("//input[@type='text']").send_keys("wangyanyan")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        driver.find_element_by_link_text(u"高级搜索").click()
        driver.find_element_by_xpath("//td[3]/label").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").click()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys(u"新华网")
        driver.find_element_by_xpath("//button[@type='button']").click()
        
        time.sleep(10)
        list_num=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        print(list_num)
        assert int(list_num) > 0
    
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
