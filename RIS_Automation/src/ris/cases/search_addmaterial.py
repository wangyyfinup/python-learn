# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''信息列表-加入素材测试'''
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
        #点击筛选论坛类型的信息（为了避免出现微博转发类型的信息处于合并后的第一条中）
        driver.find_element_by_id("info_13").click()
        time.sleep(5)
        #在信息列表第一条新闻信息下方点击加入素材
        driver.find_element_by_xpath("//*[@id='report']/table/tbody/tr[1]/div[2]/div[3]/a").click()
        time.sleep(1)
        #验证弹框标题正确
        pop_up_win_title=driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div[1]/p/span").text
        assert pop_up_win_title=="加入素材"
        #输入新的素材分组名称
        now= time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/div/input").send_keys("zdhcs_02-"+now)
        time.sleep(1)
        #点击添加，添加素材分组
        driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/button/span").click()
        #WebDriverWait(driver,10).until(expected_conditions.text_to_be_present_in_element_value("/html/body/div[18]"))
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("/html/body/div[2]/div"))
        time.sleep(2)
        #点击确定，完成添加素材
        driver.find_element_by_css_selector("body > div.modal-height.v-transfer-dom > div.ivu-modal-wrap > div > div > div.ivu-modal-footer > div > button.ivu-btn.ivu-btn-primary").click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath("/html/body/div[2]/div"))
        time.sleep(3)
        
        #进入素材库，将创建的测试数据删除
        #////待考虑删除的方式
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
