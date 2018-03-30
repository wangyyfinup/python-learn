# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time,datetime

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''将搜索加入追踪测试'''
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

        #点击加入监测按钮，验证弹出弹框
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[1]/div/div[3]/span[2]/a").click()
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]").is_displayed()
        
        #验证当前默认进入的是高级配置,高级配置tab是高亮状态
        tab_name=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]").text
        assert tab_name=="追踪任务高级配置"
        tab_class_name=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]").get_attribute("class")
        assert tab_class_name=="ivu-tabs-tab ivu-tabs-tab-active"
        
        #开始输入事件配置信息，新建事件
        #输入事件名称
        name_now=time.strftime("%m%d%H%M%S",time.localtime(time.time()))
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div/input").send_keys("北京-加入高级事件"+name_now)
        time.sleep(1)
        
        #输入事件监测范围
        #设置开始时间为当前时间的前一天
        now = datetime.datetime.now()
        yes_time = now + datetime.timedelta(days=-1)
        starttime = yes_time.strftime('%Y-%m-%d %H:%M')
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/input").clear()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/input").send_keys(starttime)
        time.sleep(1)
        #设置结束时间为今后20天
        later_time=now+datetime.timedelta(days=+20)
        endtime=later_time.strftime("%Y-%m-%d %H:%M")
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/input").clear()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div/input").send_keys(endtime)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[2]/div[1]/label").click()
        time.sleep(1)      
        #验证事件当前是启用状态
        task_status=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[2]/div/div/span/span/span").text
        assert task_status=="启用"
        #验证默认关键词
        key_words=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/div/div/div/textarea").get_attribute("value")
        assert key_words=="北京"
        time.sleep(1)
        #验证匹配方式
        num=[2,3,1]
        for j in num:
            driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[3]/div/div/div/label["+str(j)+"]/span/input").click()
            time.sleep(1)
        
        #关键词词频暂不设置
        
        #验证预警是关闭状态
        warn_status=driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[3]/div[2]/div/div/div/div/span/span/span").text
        assert warn_status=="停用"
        
        #点击预览，验证弹出预览弹框，预览成功则关闭弹框
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[2]/div/button[1]").click()
        time.sleep(5)
        winname=driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div/div[1]/div").text
        if winname=='结果预览':
            print('成功打开预览窗口')
            driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/div[3]/div/button').click()
            time.sleep(2)
        else:
            pass
        #点击完成，完成事件配置
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div/div[2]/div/button[2]").click()
        time.sleep(2)
        
        #验证事件是否新建成功,进入事件模块，检查事件是否存在
        #跳转到事件追踪模块
        driver.find_element_by_xpath("//*[@id='sysHead_div']/li[3]").click()
        time.sleep(3)
        #先获取整个事件列表，再验证是否有刚才创建的那个事件
        event_list=driver.find_elements_by_xpath("//*[@id='app']/div[2]/div[1]/div/div")
        for i in range(1,len(event_list)+1):
            event_name=driver.find_element_by_xpath("//*[@id='app']/div[2]/div[1]/div/div["+str(i)+"]/div[1]/div[2]/div[1]/label").get_attribute("title")
            if event_name==("北京-加入高级事件"+name_now):
                break
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
