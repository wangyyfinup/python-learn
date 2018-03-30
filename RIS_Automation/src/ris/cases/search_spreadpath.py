# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest,time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''微博传播路径测试'''
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
        #点击导航栏进入搜索模块
        driver.find_element_by_xpath("//div[@id='sysHead_div']/li[5]").click()
        #输入北京，模糊搜索
        driver.find_element_by_xpath("//*[@id='searchApp']/div[1]/div/form/div/div/div/div[1]/div/input").send_keys(u"北京")
        driver.find_element_by_css_selector("#searchApp > div.s_row.ivu-row > div > form > div > div > div > div.s-right > img").click()
        time.sleep(10)
        #验证信息列表的数量大于0
        list_num=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        assert int(list_num) > 0

        #查看新闻,微信类型信息的传播路径
        pathlist={'11':'新闻传播路径','21':'微信传播路径'}
        for key in pathlist:
            driver.find_element_by_id("info_"+str(key)).click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[3]/a[1]').click()
            time.sleep(2)
            winname=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[1]/p').text
            assert winname == pathlist[key]
            time.sleep(15)
            content=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/div/div[1]/span[1]/span').text
            assert content=="(定位此文章)"
            driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/a/i').click()
            time.sleep(2)
        #查看微博类型的传播路径
        driver.find_element_by_id("info_22").click()
        time.sleep(3)
        driver.find_element_by_css_selector('#report > table > tbody > tr:nth-child(2) > div.clist > div.info > a:nth-child(6)').click()
        time.sleep(2)
        winname=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[1]/p').text
        assert winname == "微博传播路径"
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/a/i').click()


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
