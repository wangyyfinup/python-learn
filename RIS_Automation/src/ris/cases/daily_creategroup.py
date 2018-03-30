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
        #检查导航栏
        classlist={"1":"index_add","2":"tree-menu-msg","3":"layout-content","4":"weiboSpan","5":"icon-cusor","6":"reportItemSpan","7":"twitterSpan"}
        for key in classlist:
            driver.find_element_by_xpath('//*[@id="sysHead_div"]/li['+str(key)+']').click()
            sleep(1)
            s = driver.find_elements_by_css_selector('[class='+classlist[key]+']')
            assert len(s) !=0

        #跳转到日常监测模块
        driver.find_element_by_xpath("//*[@id='sysHead_div']/li[2]").click()
        sleep(1)
        
        #测试创建任务分组
        driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div[1]/img").click()
        sleep(2)
        driver.find_element_by_xpath("//*[@id='taskGroupName']/input").send_keys('测试专用分组')
        sleep(1)
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]/span').click()
        sleep(2)
        groupname=driver.find_element_by_css_selector('[title=测试专用分组]').text
        assert groupname == "测试专用分组"

    def tearDown(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()