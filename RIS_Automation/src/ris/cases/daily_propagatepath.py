'''
查看新闻，微博，微信类型的信息传播路径
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
        sleep(1)
        driver.find_element_by_css_selector('[title=北京欢迎你-初级]').click()
        sleep(2)

        #查看新闻,微信类型信息的传播路径
        pathlist={'2':'新闻传播路径','5':'微信传播路径'}
        for key in pathlist:
            driver.find_element_by_xpath('//*[@id="infoTypeId"]/span['+str(key)+']').click()
            sleep(3)
            driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[3]/a[1]').click()
            winname=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[1]/p').text
            assert winname == pathlist[key]
            sleep(15)
            content=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[2]/div/div/div[1]/span[1]/span').text
            assert content=="(定位此文章)"
            driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/a/i').click()
            sleep(2)
        #查看微博类型的传播路径
        driver.find_element_by_xpath('//*[@id="infoTypeId"]/span[4]').click()
        sleep(3)
        driver.find_element_by_css_selector('#report > table > tbody > tr:nth-child(2) > div.clist > div.info > a:nth-child(6)').click()
        winname=driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/div[1]/p').text
        assert winname == "微博传播路径"
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[7]/div[2]/div/div/a/i').click()
 
    
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()