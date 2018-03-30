'''
实现监测任务切换，时间范围筛选，信息类型筛选，信息类型多选验证，内容、情感筛选
'''
#coding=Utf-8
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
        sleep(1)
        #跳转到日常监测模块
        driver.find_element_by_xpath("//*[@id='sysHead_div']/li[2]").click()
        sleep(2)
        #切换监测任务
        driver.find_element_by_css_selector('[title=北京欢迎你-初级]').click()
        sleep(10)
        num1=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        driver.find_element_by_css_selector('[title=北京欢迎你-高级]').click()
        sleep(10)
        num2=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        assert num1 != num2
        
        #时间范围筛选
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[1]/div/span[4]').click()
        searchbutton=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[1]/div/span[5]/button').get_attribute("title")
        assert searchbutton == "搜索"
        sleep(3)
        driver.find_element_by_xpath('//*[@id="firstDay"]').click()
        sleep(3)
        dayinfo=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        driver.find_element_by_xpath('//*[@id="lastWeek"]').click()
        sleep(5)
        weekinfo=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        driver.find_element_by_xpath('//*[@id="lastMonth"]').click()
        sleep(5)
        mouthinfo=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
        mouth=int(mouthinfo)
        week=int(weekinfo)
        day=int(dayinfo)
        assert (mouth>=week)&(week>=day)
        
        pathlist={'0':'//*[@id="infoTypeCheckAllInfo"]',
                   '1':'//*[@id="infoTypeId"]/span[2]',
                   '2':'//*[@id="infoTypeId"]/span[3]',
                   '3':'//*[@id="infoTypeId"]/span[4]',
                   '4':'//*[@id="infoTypeId"]/span[5]',
                   '5':'//*[@id="infoTypeId"]/span[6]',
                   '6':'//*[@id="infoTypeId"]/span[7]',
                   '7':'//*[@id="infoTypeId"]/span[8]',
                   '8':'//*[@id="infoTypeId"]/span[9]',
                   '9':'//*[@id="infoTypeId"]/span[10]'}
        
        #检查信息类型筛选条件是否都存在,分别点击不同的信息类型，判断信息列表中第一条数据的信息类型图标是否与选择的信息类型一致
        info_condition=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[2]/div/span').text
        assert info_condition == "信息类型："
        infotype_list=['全部','新闻','论坛','微博','微信','APP','平媒','境外','Twitter','Facebook']
        img_list=['','news.4b644f3.png','','wb.aa90135.png','wechat.3d10cb8.png','app.de71dd8.png','pm.abf4861.png','','twitter.ec7c7c0.png','facebook.4d71ebd.png']
        for key in pathlist:
            infotype=driver.find_element_by_xpath(''+pathlist[key]+'').text
            assert infotype==infotype_list[int(key)]
            driver.find_element_by_xpath(''+pathlist[key]+'').click()
            sleep(5)
            if (infotype=="全部" or infotype=="论坛" or infotype=="境外"):
                pass
            else:
                #验证信息列表的数量大于0
                list_num=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
                assert int(list_num) > 0
                img=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[1]/img').get_attribute("src")
                assert img == "http://103.66.33.159:8083/static/img/"+img_list[int(key)]
          
        #信息类型多选验证,点击多选，选择微博，微信，Twitter,Facebook类型，点击确定
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[2]/span').click()
        confirm=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/button[1]/span').text
        cancle=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/button[2]/span').text
        assert confirm =="确定"
        assert cancle =="取消"
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/label').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/label').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[3]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[4]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[8]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[1]/label[9]').click()
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[3]/div[2]/div[2]/button[1]/span').click()
        #验证多选选择的几个类型是高亮的，其他非高亮.
        for key1 in pathlist:
            lightinfo=driver.find_element_by_xpath(''+pathlist[key1]+'').get_attribute("class")
            key2=int(key1)
            if (key2 in [3,4,8,9]):
                assert lightinfo=="condition_right info-type activecolor"
            else:
                assert lightinfo=="condition_right info-type"
        #展开按钮
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[4]/div/div').click()
        contenttype=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[5]/div/span').text
        emotiontype=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[6]/div/span').text
        assert contenttype == "内容类型："
        assert emotiontype == "情感倾向："
        #确认是否默认“全部”被选中
        lightcontent=driver.find_element_by_xpath('//*[@id="contentTypeAll"]').get_attribute("class")
        assert lightcontent == "condition_right content-type activecolor"
        lightemotion=driver.find_element_by_xpath('//*[@id="emotionTypeAll"]').get_attribute("class")
        assert lightemotion == "condition_right emotion-type activecolor"
        #判断内容情感倾向各类型的按钮能否点击
        arr1=[3,2]
        for i in arr1:
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[5]/div/div/span['+str(i)+']').click()
            sleep(1)
            lighttype=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[5]/div/div/span['+str(i)+']').get_attribute("class")
            assert lighttype == "condition_right content-type activecolor"
        arr2=[4,3,2]       
        for j in arr2:
            driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[6]/div/div/span['+str(j)+']').click()
            sleep(1)
            lighttype=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[6]/div/div/span['+str(j)+']').get_attribute("class")
            assert lighttype == "condition_right emotion-type activecolor"
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()  