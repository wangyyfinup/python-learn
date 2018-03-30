# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
    
    def test_untitled_test_case(self):
        u'''信息列表相似合并测试'''
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
        #验证相似合并标签是否存在
        mergeLabel=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[4]/span[1]").text
        print(mergeLabel)
        assert mergeLabel=="相似合并"
        #验证初始时是没有打开合并开关
        offbutton=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[4]/span[2]/span/span").text
        print(offbutton)
        assert offbutton=="OFF"
        #点击打开相似合并开关
        driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[4]/span[2]").click()
        time.sleep(5)
        #验证现在相似合并开关已经打开
        onbutton=driver.find_element_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[4]/span[2]/span/span").text
        assert onbutton=="ON"
        #点击筛选新闻类型的信息（为了避免出现微博转发类型的信息处于合并后的第一条中）
        driver.find_element_by_id("info_11").click()
        time.sleep(5)
        #验证第一条新闻类型信息的右下方出现 合并文章数
        #mergeinfo=driver.find_elements_by_xpath("//*[@id='report']/table/tbody/tr[1]/div[2]/div[3]/span[6]")
        mergeinfo=driver.find_element_by_css_selector("#report > table > tbody > tr:nth-child(1) > div.clist > div.info > span.similarnum.cursor_pointer").text
        mergeinfo_list=mergeinfo.split('：')
        mergelabel=mergeinfo_list[0]
        mergenum=mergeinfo_list[1]
        assert mergelabel=="合并文章数"
        #获取到合并文章数目，验证它大于0
        assert int(mergenum)>=1
        #点击合并文章数链接，弹出相似文章弹框
        driver.find_element_by_css_selector("#report > table > tbody > tr:nth-child(1) > div.clist > div.info > span.similarnum.cursor_pointer").click()
        time.sleep(5)
        pop_win_title=driver.find_element_by_xpath("//*[@id='sameDocModal']/div[2]/div/div/div/div[1]/span").text
        assert pop_win_title=="合并文章"
        #在弹框中点击一条信息的标题，验证打开正文详情页
        current_win=driver.current_window_handle
        similar_doc_title=driver.find_element_by_xpath("//*[@id='report']/div/table/tbody/tr[1]/div/div[1]/span[2]/a").text
        driver.find_element_by_xpath("//*[@id='report']/div/table/tbody/tr[1]/div/div[1]/span[2]/a").click()
        time.sleep(2)
        print(similar_doc_title)
        #在新打开的tab页获取正文中的标题，验证是否与相似合并弹框中获取到的一致
        allhandles=driver.window_handles
        for handle in allhandles:
            if handle !=current_win:
                driver.switch_to.window(handle)
                detail_title=driver.find_element_by_xpath("//*[@id='detail']/div/div[1]/div[1]/div[1]").text
                print(detail_title)
                assert detail_title==similar_doc_title
                driver.close()
        
        #关闭弹窗，回到原浏览器页面，验证文章数排序
        driver.switch_to.window(current_win)
        driver.find_element_by_xpath("//*[@id='sameDocModal']/div[2]/div/div/a/i").click()
        time.sleep(3)
        sortimg_list=driver.find_elements_by_xpath("//*[@id='searchComplexApp']/div[2]/div[6]/div[2]/div[1]/div[2]/img")
        print(sortimg_list)
        num=1
        for sortimg in sortimg_list:
            print(sortimg.get_attribute("title"))
            if num<=3:
                assert sortimg.get_attribute("title")=="按时间排序"
                num=num+1
            elif num<=6:
                assert sortimg.get_attribute("title")=="按相关度排序"
                num=num+1
            else:
                assert sortimg.get_attribute("title")=="按相似文章数排序"
                num=num+1
                
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
