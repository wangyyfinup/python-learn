'''

'''
# coding UTF-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains

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
        sleep(10)
        driver.find_element_by_css_selector("[title=北京欢迎你-初级]").click()
        sleep(25)
        #判断合并前后数据是否变化
        num1=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[3]/span[2]/span').click()
        sleep(25)
        num2=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        assert num1 != num2
        driver.find_element_by_css_selector('[class="similarnum cursor_pointer"]').click()
        sleep(15)
        winname=driver.find_element_by_xpath('//*[@id="sameDocModal"]/div[2]/div/div/div/div[1]/span').text
        assert winname == "合并文章"
        sleep(6)
        #获取信息列表窗口句柄
        infolist_window=driver.current_window_handle
        #打开正文详情
        driver.find_element_by_xpath('//*[@id="report"]/div/table/tbody/tr[1]/div/div[1]/span[2]/a').click()
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
        sleep(2)
        #打开原文
        driver.find_element_by_xpath('//*[@id="report"]/div/table/tbody/tr[1]/div/div[4]/a').click()
        all_handles=driver.window_handles
        assert len(all_handles)>0
        if len(all_handles)>1:
            for handle in all_handles:
                if handle==infolist_window:
                    pass
                else:
                    driver.switch_to.window(handle)
                    driver.close()
                    driver.switch_to.window(infolist_window)
        #加入素材，验证弹窗
        driver.find_element_by_xpath('//*[@id="report"]/div/table/tbody/tr[1]/div/div[3]/a').click()
        sleep(2)
        pop_name1=driver.find_element_by_xpath('/html/body/div[18]/div[2]/div/div/div[1]/p/span').text
        assert pop_name1 == "加入素材"
        #新建素材分组
        now= time.strftime("%m-%d",time.localtime(time.time()))
        driver.find_element_by_xpath('/html/body/div[18]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/div/input').send_keys("dailymonitor-"+now)
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[18]/div[2]/div/div/div[2]/div/form/table/tr[2]/td[2]/div/div/button/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div'))
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[18]/div[2]/div/div/div[3]/div/button[1]/span').click()
        WebDriverWait(driver,10).until(lambda x:x.find_element_by_xpath('/html/body/div[18]/div')) 
        sleep(3)
        #关闭相似合并窗口
        above=driver.find_element_by_xpath('//*[@id="sameDocModal"]/div[2]/div/div/a/i')
        ActionChains(driver).move_to_element(above).click().perform()
        #相似文章数排序
        num3=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[3]/span[6]').text
        sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[2]/div[1]/img[9]').click()
        sleep(3)
        num4=driver.find_element_by_css_selector('[class="similarnum cursor_pointer"]').text
        assert num4<num3
                
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()