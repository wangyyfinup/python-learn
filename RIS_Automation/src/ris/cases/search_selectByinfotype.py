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
        u'''按信息类型筛选测试'''
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
        time.sleep(10)
        #验证信息列表的数量大于0
        list_num=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
        assert int(list_num) > 0
        #检查信息类型筛选条件是否都存在,分别点击不同的信息类型，判断信息列表中第一条数据的信息类型图标是否与选择的信息类型一致
        info_condition=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[2]/div[1]/span").text
        assert info_condition == "信息类型："
        infotype_list=['全部','新闻','论坛','微博','微信','APP','平媒','境外','Twitter','Facebook']
        infonum_list=['all','11','13','22','21','31','12','41','42','43']
        img_list=['','news.4b644f3.png','','wb.aa90135.png','wechat.3d10cb8.png','app.de71dd8.png','pm.abf4861.png','','twitter.ec7c7c0.png','facebook.4d71ebd.png']
        for i in range(0,10):
            infotype=driver.find_element_by_id("info_"+str(infonum_list[i])).text
            assert infotype==infotype_list[i]
            driver.find_element_by_id("info_"+str(infonum_list[i])).click()
            time.sleep(3)
            if (infotype=="全部" or infotype=="论坛" or infotype=="境外"):
                pass
            else:
                #验证信息列表的数量大于0
                list_num=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[1]/span[2]").text
                assert int(list_num) > 0
                #print(infotype,list_num)
                img=driver.find_element_by_xpath("//*[@id='report']/table/tbody/tr[1]/div[2]/div[1]/img").get_attribute("src")
                assert img == "http://10.129.0.240:8083/static/img/"+img_list[i]
        
        #信息类型多选验证,点击多选，选择新闻、微博、平媒类型，点击确定
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[2]/div[2]/span").click()
        confirm=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[3]/div[2]/div/button[1]/span").text
        cancle=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[3]/div[2]/div/button[2]/span").text
        assert confirm =="确定"
        assert cancle =="取消"
        driver.find_element_by_xpath("//*[@id='11']/span/input").click()
        driver.find_element_by_xpath("//*[@id='22']/span/input").click()
        driver.find_element_by_xpath("//*[@id='12']/span/input").click()
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[3]/div[2]/div/button[1]/span").click()
        #验证多选选择的几个类型是高亮的，其他非高亮.
        for i in range(0,10):
            info_class=driver.find_element_by_xpath("//*[@id='info_"+str(infonum_list[i])+"']").get_attribute("class")
            if i==0:
                pass
            elif (i==1 or i==3 or i==6 or i==9):
                print(i,info_class)
                assert info_class=="condition_right span-cusor infoClass mactive" 
            else:
                #print(i,info_class)
                assert info_class=="condition_right span-cusor infoClass"
                
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
