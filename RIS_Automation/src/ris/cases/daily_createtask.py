'''
实现新建监测任务，修改任务，删除任务的操作
'''

#coding=Utf-8

from selenium import webdriver
#from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import unittest
import datetime


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
       
        #新建任务
        driver.find_element_by_css_selector('[title=测试专用分组]').click()
        driver.find_element_by_xpath('//*[@id="taskGroupTree"]/div/div[1]/div[2]/div/span/i').click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/form/div/div/div[1]/div/div[2]/input").send_keys('北京欢迎你-初级')
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button/span').click()
        #选择匹配方式
        num=[2,3,1]
        for i in num:
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]/form/div[2]/div[1]/div[1]/div/div/div/label['+str(i)+']/span/input').click()
            sleep(1)
        #关键词配置
        driver.find_element_by_xpath('//*[@id="areaWords"]/textarea').send_keys('北京')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="organPersonWords"]/textarea').send_keys('发展')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="eventWords"]/textarea').send_keys('经济')
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]/span").click()
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]/form/div/div[1]/div/div/span/div[1]/div[1]/div/input').clear()
        #获取开始时间（设置为当前时间的前一天）
        now = datetime.datetime.now()
        yes_time = now + datetime.timedelta(days=-14)
        starttime = yes_time.strftime('%Y-%m-%d %H:%M')
        sleep(1)
        #监测范围
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]/form/div/div[1]/div/div/span/div[1]/div[1]/div/input').send_keys(starttime)
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]/form/div').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[1]/div[4]/form/div/div[2]/div/div/label/span/input').click()
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]/span').click()
        sleep(2)
        #点击预览窗口
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]').click()
        sleep(2)
        winname=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[1]/div').text
        assert winname == "结果预览"
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/div/button/span').click()
        sleep(2)
        #完成配置
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[3]/span').click()
        sleep(2)
        #判断是否创建成功
        taskname=driver.find_element_by_css_selector('[title=北京欢迎你-初级]').text
        assert taskname == "北京欢迎你-初级"
        
        #新建高级监测任务
        driver.find_element_by_css_selector('[title=测试专用分组]').click()
        driver.find_element_by_css_selector('[title=测试专用分组]').click()
        driver.find_element_by_xpath('//*[@id="taskGroupTree"]/div/div[1]/div[2]/div/span/i').click()
        sleep(1)
        #跳转到高级配置table页
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[3]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[1]/input').send_keys('北京欢迎你-高级')
        sleep(2)
        #关键词配置 
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[1]/div/div/div[1]/textarea').send_keys('(北京）|（经济）|（usa)')
        sleep(2)
        #检查匹配方式
        num=[2,3,1]
        for j in num:
            driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[2]/div[2]/div[3]/div/div/div/label['+str(j)+']/span/input').click()
            sleep(1)
            #监测范围配置
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[1]/div/div/span/div[1]/div[1]/div/input').clear()
        #获取开始时间（设置为当前时间的前一天）
        now = datetime.datetime.now()
        yes_time = now + datetime.timedelta(days=-3)
        starttime = yes_time.strftime('%Y-%m-%d %H:%M')
        sleep(1)

        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[1]/div/div/span/div[1]/div[1]/div/input').send_keys(starttime)
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div').click()
        sleep(2)
        #选择信息类型
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div[2]/div/form/div[3]/div[2]/div[2]/div/div/div[1]/label[1]/span/input').click()
        sleep(2)
        #点击预览窗口
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[1]/span').click()
        sleep(2)
        winname=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[1]/div').text
        assert winname == "结果预览"
        driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/div[3]/div/button/span').click()
        sleep(2)
        #完成配置
        driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/button[2]/span').click()
        sleep(2)
        #判断是否创建成功
        taskname=driver.find_element_by_css_selector('[title=北京欢迎你-高级]').text
        assert taskname == "北京欢迎你-高级"

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()

