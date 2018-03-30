# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''信息搜索信息列表翻页测试'''
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
        
        #拖动浏览器的滚动条，到页面最底部
        js="var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)
        time.sleep(2)
        #点击回到顶部
        driver.find_element_by_xpath('//*[@id="report"]/div/div/img').click()
        time.sleep(3)
        #测试翻页，分别点击1、2、3、4页，然后分别点击下一页、上一页
        apage=[2,3,4,5,12,1]
        for i in apage:
            driver.execute_script(js)
            time.sleep(2)
            driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[3]/ul[1]/li["+str(i)+"]").click()
            time.sleep(10)
            if i==12:
                tag_classname=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[3]/ul[1]/li[6]").get_attribute("class")
                print("cc",tag_classname)
                assert tag_classname=="active"
            elif i==1:
                tag_classname=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[3]/ul[1]/li[5]").get_attribute("class")
                print("bb",tag_classname)
                assert tag_classname=="active"
            else:
                tag_classname=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[3]/ul[1]/li["+str(i)+"]").get_attribute("class")
                print("aa",tag_classname)
                assert tag_classname=="active"
                
        #设置每页显示的信息条数，并判断是否生效
        alistnum=[1,2,3,4]
        apagenum=[10,20,50,100]
        #zip函数合并两个数组
        for listnum,pagenum in zip(alistnum,apagenum):
            #获取每页显示信息条数
            driver.find_element_by_xpath('//*[@id="searchComplexApp"]/div[2]/div[6]/div[2]/div[3]/ul[2]/li/div/div[1]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="searchComplexApp"]/div[2]/div[6]/div[2]/div[3]/ul[2]/li/div/div[2]/ul[2]/li['+str(listnum)+']').click()
            time.sleep(10)
            driver.execute_script(js)
            list_num=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr['+str(pagenum)+']/div[2]/div[1]/span[1]').text
            listnum=int(list_num)
            if listnum == pagenum:
                pass
            else:
                print("显示页码设置未生效")
                
                
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
