'''
首页添加日常监测的统计图
'''
# coding UTF-8
from selenium import webdriver
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
        
        
        driver.find_element_by_xpath('//*[@id="index"]/div[1]/img').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/i[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[1]/div[1]/div/div/div[2]/ul[2]/li[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[1]/div[2]/div/div/div[1]/i[2]').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/ul[2]/li[2]').click()
        for i in [2,3,1]:
            driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[1]/div[2]/div/div['+str(i)+']/label/span[1]/input').click()
            if int(i)==2:
                driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[2]/div/div[2]/img').click()
                sleep(1)
            elif int(i)==3:
                for j in range(1,7):
                    driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[2]/div['+str(j)+']/div[2]').click()
                    sleep(1)
            else:
                driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[2]/div[1]/div[2]/img').click()
                driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[2]/div[2]/div[2]/div/form/div[1]/div/div[2]/div[2]/div[2]/div[2]/img').click()
                sleep(1)
        driver.find_element_by_xpath('//*[@id="index_portal"]/div[2]/div/div/div[3]/div/button[1]/span').click()
        sleep(10)
        
    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()