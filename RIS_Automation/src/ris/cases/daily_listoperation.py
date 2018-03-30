'''
检查信息列表、统计图，打开正文详情页、原文页，添加素材，标记为不相关，空操作
'''
#coding=Utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import time
import unittest


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_untitled_test_case(self):   
        driver = self.driver
        driver.get('http://103.66.33.159:8083/login')
        sleep(1)
        #用户登录
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[2]/div/div/input").clear()
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[2]/div/div/input").send_keys('zdhcs_01')
        sleep(1)
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[3]/div/div/input").clear()
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[3]/div/div/input").send_keys('1q2w3e4r5t%')
        sleep(1)
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[4]/div/div/div/input").send_keys('Qw5e!')
        driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[5]/div/button/span/span").click()
        sleep(2)
    
        #跳转到日常监测模块
        driver.find_element_by_xpath("//*[@id='sysHead_div']/li[2]").click()
        sleep(1)
        driver.find_element_by_css_selector('[title=北京欢迎你-初级]').click()
        sleep(3)
        
        #检查信息列表和统计图
        for i in [2,3,4,1]:
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[10]/div['+str(i)+']/label').click()
            sleep(1)
            int(i)
            if i == 2:
                info=driver.find_element_by_xpath('//*[@id="daily_stat_area1"]/div[1]/div[1]').text
                emotion=driver.find_element_by_xpath('//*[@id="daily_stat_area1"]/div[2]/div/div[1]/div[1]').text
                assert info == "信息趋势图"
                assert emotion == "情感分析"
            elif i == 3:
                infotype=driver.find_element_by_xpath('//*[@id="daily_stat_area2"]/div[1]/div/div[1]/div[1]').text
                netstation=driver.find_element_by_xpath('//*[@id="daily_stat_area2"]/div[1]/div/div[2]/div[1]').text
                mediatop=driver.find_element_by_xpath('//*[@id="daily_stat_area2"]/div[2]/div').text
                assert infotype == "信源类型分布"
                assert netstation == "网站地域分析"
                assert mediatop == "媒体发布TOP3"
            elif i == 4:
                hotword=driver.find_element_by_xpath('//*[@id="daily_stat_area3"]/div[1]/div/div[1]/div[1]').text
                human=driver.find_element_by_xpath('//*[@id="daily_stat_area3"]/div[1]/div/div[2]/div[1]').text
                organization=driver.find_element_by_xpath('//*[@id="daily_stat_area3"]/div[2]/div/div[1]/div[1]').text
                region=driver.find_element_by_xpath('//*[@id="daily_stat_area3"]/div[2]/div/div[2]/div[1]').text
                assert hotword == "热词推荐"
                assert human == "提及人物"
                assert organization == "提及机构"
                assert region == "提及地域"
            else:
                sleep(3)
                infonum=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
                assert infonum != 0
        num1=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/div[1]/input').send_keys('政策')
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/img[1]').click()
        sleep(2)
        num2=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        assert num1>num2
        driver.find_element_by_css_selector('[title=北京欢迎你-初级]').click()
        
        sleep(3)
        #获取信息列表窗口句柄
        infolist_window=driver.current_window_handle
        #打开正文
        for key in range(1,11):           
            driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr['+str(key)+']/div[2]/div[1]/span[2]').click()            
            all_handles=driver.window_handles
            assert len(all_handles)>0
            if len(all_handles)>1:
                for handle in all_handles:
                    if handle==infolist_window:
                        pass
                    else:
                        driver.switch_to.window(handle)
                        sleep(3)
                        title=driver.find_element_by_xpath('//*[@id="head"]/div[1]/div/ul/div').text
                        assert len(title) != 0
                        driver.close()
                        driver.switch_to.window(infolist_window)                        
        #打开原文
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[2]/span').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[5]/span/input').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[7]/span/input').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[8]/span/input').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[9]/span/input').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/button[1]/span').click()
        sleep(5)
        infolist_window=driver.current_window_handle
        for j in range(1,11):
            driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr['+str(j)+']/div[2]/div[4]/a').click()
            all_handles=driver.window_handles
            assert len(all_handles)>0
            if len(all_handles)>1:
                for handle in all_handles:
                    if handle==infolist_window:
                        pass
                    else:
                        driver.switch_to.window(handle)
                        sleep(1)
                        driver.close()
                        driver.switch_to.window(infolist_window)
                        sleep(2)
                        sleep(2)
                        js="var q=document.documentElement.scrollTop=500"  
                        driver.execute_script(js)
        #加入素材,选取信息列表第一条信息加入素材
        driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[1]/input').click()
        sleep(1)
        #加入素材，验证弹窗
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/img[2]').click()
        pop_name1=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[1]/p/span').text
        assert pop_name1 == "加入素材"
        #新建素材分组
        now= time.strftime("%m-%d-%H-%M",time.localtime(time.time()))
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/div/input').send_keys("dailymonitor-"+now)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/button/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div')) 
        sleep(3)
        #加入素材，将信息列表第二条信息通过右下角的加入素材按钮 来添加 
        #加入素材，验证弹窗
        driver.find_element_by_xpath('//*[@id="infoTypeId"]/span[2]').click()
        sleep(3)
        driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[3]/a[3]').click()
        pop_name2=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[1]/p/span').text
        assert pop_name2 == "加入素材"
        #新建素材分组
        now= time.strftime("%m-%d-%H",time.localtime(time.time()))
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/div/input').send_keys("dailymonitor-"+now)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/button/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div')) 
        sleep(3)
        #批量加入素材
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/input').click()
        sleep(1)
        #加入素材，验证弹窗
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/img[2]').click()
        pop_name3=driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[1]/p/span').text
        assert pop_name3 == "加入素材"
        #新建素材分组
        now= time.strftime("%m-%d",time.localtime(time.time()))
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/div/input').send_keys("dailymonitor-"+now)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/button/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div[3]/div/button[1]/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div')) 
        sleep(3)

        #批量标记不相关
        driver.find_element_by_xpath('//*[@id="infoTypeCheckAllInfo"]').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/input').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/button').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        sleep(2)
        driver.find_element_by_xpath('//*[@id="infoTypeId"]/span[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[3]/a[2]').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))

        #未选信息点击添加素材按钮
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/img[2]').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        #未选信息点击标记不相关按钮
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/button').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        #未选信息点击导出按钮
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[2]/img[3]').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()