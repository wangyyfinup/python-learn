'''
Created on 2018年3月23日

@author: editor01
'''
# coding UTF-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

#登录函数
def login(username,password):
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[2]/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[2]/div/div/input").send_keys(username)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[3]/div/div/input").clear()
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[3]/div/div/input").send_keys(password)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[4]/div/div/div/input").send_keys('Qw5e!')
    driver.find_element_by_xpath("//*[@id='login']/div[2]/div[2]/form/div[5]/div/button/span/span").click()
        
driver = webdriver.Chrome()
driver.get('http://103.66.33.159:8083/login')
driver.maximize_window()
sleep(1)
#用户登录
login("zdhcs_01","1q2w3e4r5t%")
sleep(1)
#跳转到日常监测模块
driver.find_element_by_xpath("//*[@id='sysHead_div']/li[2]").click()
sleep(1)

#查看监测任务
driver.find_element_by_css_selector("[title='两会']").click()
sleep(5)
#获取信息量
info_num=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[11]/div[1]/span[2]').text
if info_num == 0:
    print('信息列表未显示检索结果')
else:
    pass

#返回顶部
page_list=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[12]/div[2]/ul[2]/li/div')
ActionChains(driver).click(page_list).perform() 
sleep(1)
driver.find_element_by_xpath('//*[@id="report"]/div/div/img').click()
sleep(3)
#翻页
title=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[1]/span[2]').text
sleep(3)
apage=[3,4,5,6,7,8,9,10,11,12,1]
for i in apage:
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[12]/div[2]/ul[1]/li['+str(i)+']/a').click()
    sleep(10)
    title_01=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr[1]/div[2]/div[1]/span[2]').text
    if title_01 == title :
        print('翻页不成功')
    else:
        pass
    title = title_01


#设置每页显示的信息条数，并判断是否生效
alistnum=[1,2,3,4]
apagenum=[10,20,50,100]
#zip函数合并两个数组
for listnum,pagenum in zip(alistnum,apagenum):
    #获取每页显示信息条数
    page_list=driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[12]/div[2]/ul[2]/li/div')
    ActionChains(driver).click(page_list).perform() 
    sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div[1]/div[2]/div[12]/div[2]/ul[2]/li/div/div[2]/ul[2]//li['+str(listnum)+']').click()
    sleep(5)
    list_num=driver.find_element_by_xpath('//*[@id="report"]/table/tbody/tr['+str(pagenum)+']/div[2]/div[1]/span[1]').text
    listnum=int(list_num)
    if listnum == pagenum:
        pass
    else:
        print("显示页码设置未生效")

sleep(1)
driver.quit()