# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        
    def test_untitled_test_case(self):
        u'''按微信账号精确搜索测试'''
        driver = self.driver
    
        #登录
        driver.get("http://10.129.0.240:8083/login")
        driver.find_element_by_xpath("//input[@type='text']").send_keys("zdhcs_02")
        driver.find_element_by_xpath("//input[@type='password']").send_keys("1q2w3e4r5t%")
        driver.find_element_by_xpath("(//input[@type='text'])[2]").send_keys("Qw5e!")
        driver.find_element_by_xpath("//button[@type='button']").click()
        #点击导航栏，进入信息搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        #在信息搜索页面点击高级搜索
        driver.find_element_by_link_text(u"高级搜索").click()
        #单选微信信息类型
        driver.find_element_by_xpath("//td[4]/label").click()
        #输入新华社微信公众号，点击搜索
        driver.find_element_by_xpath("(//input[@type='text'])[7]").send_keys(u"新华社")
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(5)
        #验证信息列表的数量大于0 
        list_num=driver.find_element_by_xpath("//div[@id='searchComplexApp']/div[2]/div[6]/div[2]/div/div/span[2]").text
        assert int(list_num)>0
        #验证信息列表中第一条信息的图标是微信类型
        img=driver.find_element_by_xpath("//div[@id='report']/table/tbody/tr/div[2]/div/img").get_attribute("src")
        assert img=="http://10.129.0.240:8083/static/img/wechat.3d10cb8.png"
        #验证信息列表第一条信息下方展示的公众号名称是“新华社”
        weiChatNum=driver.find_element_by_xpath("//div[@id='report']/table/tbody/tr/div[2]/div[3]/span").text
        assert weiChatNum=="新华社"
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

