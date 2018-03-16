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
        u'''热搜词测试'''
        driver = self.driver
        driver.get("http://10.129.0.240:8083/login")
       
        driver.find_element_by_xpath("//input[@type='text']").send_keys("wangyanyan")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
    
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        time.sleep(10)
        driver.find_element_by_xpath("//div[@id='searchApp']/div[2]/div[2]/div[6]/span").click()
        time.sleep(2)

        handles = driver.window_handles
        for handle in handles:
            driver.switch_to_window(handle)
        bdtitle=driver.find_element_by_xpath("/html/body/div/div[1]/div/div[1]/div/a/img").get_attribute("title")
        print(bdtitle)
        assert bdtitle == "到百度首页"
        bdbutton=driver.find_element_by_xpath("//*[@id='su']").get_attribute("value")
        print(bdbutton)
        assert bdbutton=="百度一下"
        
    
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
