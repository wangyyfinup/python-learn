'''
Created on 2018年3月28日

@author: editor01
'''
##coding=Utf-8
from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
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
        sleep(2)
        #任务分组名称重复校验
        driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div[1]/img").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id='taskGroupName']/input").send_keys('测试专用分组')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]/span').click()
        sleep(2)
        warn=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form/div/div/span').text
        assert warn == "分组名称已存在!"
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]/span').click()
        sleep(2)
        '''
        #初级任务名称重复校验
        driver.find_element_by_xpath('//*[@id="taskGroupTree"]/div/div[1]/div[2]/div/span/i').click()
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/form/div/div/div[1]/div/div[2]/input").send_keys('北京欢迎你-初级')
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button/span').click()
        sleep(2)
        warn=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/form/div/div/div[1]/div/div[3]').text
        assert warn == "任务分组已存在"
        sleep(2)
        '''
        #高级任务名称校验
        driver.find_element_by_xpath('//*[@id="taskGroupTree"]/div/div[1]/div[2]/div/span/i').click()
        sleep(2)
        #跳转到高级配置table页
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/input').send_keys('北京欢迎你-高级')
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]').click()
        sleep(1)
        prompt=driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]').text
        assert prompt == "任务名称已存在"
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/a/div/label/i').click()
        
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()