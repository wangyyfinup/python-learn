'''
实现导航栏检查，创建，修改任务分组，
'''

#coding=Utf-8

from selenium import webdriver
#from selenium.common.exceptions import NoSuchElementException
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

#分组操作
def group_create(firstname,secondname):
    #点击新建分组按钮
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div[1]/img").click()
    sleep(1)
    #新建任务分组
    driver.find_element_by_xpath("//*[@id='taskGroupName']/input").send_keys(firstname)
    sleep(2)
    #点击取消按钮或者关闭新建窗口
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[2]').click()
    #判断取消后是否有新建的分组
    try:
        driver.find_element_by_css_selector('[title='+firstname+']').click()
    except BaseException as e:
        print (e)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div[1]/img").click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='taskGroupName']/input").send_keys(firstname)
    sleep(2)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/a/div/label/i').click()
    try:
        driver.find_element_by_css_selector('[title='+firstname+']').click()
    except BaseException as e:
        print (e)
    sleep(1)
    driver.find_element_by_xpath("//*[@id='app']/div[2]/div/div[1]/div[1]/div[1]/img").click()
    sleep(1)
    #新建任务分组
    driver.find_element_by_xpath("//*[@id='taskGroupName']/input").send_keys(firstname)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]/span').click()
    print('新建任务分组成功')
    sleep(2)
    #修改任务分组
    driver.find_element_by_css_selector('[title='+firstname+']').click()
    driver.find_element_by_xpath('//*[@id="taskGroupTree"]/div/div[1]/div[2]/div/span[1]').click()
    sleep(3)
    driver.find_element_by_xpath('//*[@id="taskGroupName"]/input').clear()
    driver.find_element_by_xpath('//*[@id="taskGroupName"]/input').send_keys(secondname) 
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[3]/div/button[1]/span').click()
    print('修改任务分组成功')
    arrgroup.append(secondname)
    sleep(2)
   
    #删除任务分组
    driver.find_element_by_css_selector('[title='+secondname+']').click()
    sleep(1)
    driver.find_element_by_xpath("//*[@id='taskGroupTree']/div/div[1]/div[2]/div/div[3]").click()
    sleep(2)
    driver.find_element_by_xpath("/html/body/div[16]/div[2]/div/div/div[3]/div/button[1]/span/span").click()
    print('删除任务分组成功')
#判断元素是否存在
def is_element_exist(classname):
    s = driver.find_elements_by_css_selector('[class='+classname+']')
    if len(s)==0:
        print ('切换不成功')
        return False
    else:
        return True     

driver = webdriver.Chrome()
driver.get('http://103.66.33.159:8083/login')
#浏览器窗口最大化
driver.maximize_window()
sleep(1)
#用户登录
login("zdhcs_01","1q2w3e4r5t%")
sleep(1)

#切换导航栏，并通过各自导航栏特有的按钮来判断是否切换成功
classlist={"1":"index_add","2":"tree-menu-msg","3":"layout-content","4":"weiboSpan","5":"icon-cusor","6":"reportItemSpan","7":"twitterSpan"}
for key in classlist:
    driver.find_element_by_xpath('//*[@id="sysHead_div"]/li['+str(key)+']').click()
    sleep(1)
    is_element_exist(classlist[key])

#跳转到日常监测模块
driver.find_element_by_xpath("//*[@id='sysHead_div']/li[2]").click()
sleep(1)

#定义一个空数组
arrgroup=[]
#创建分组
group_create('三月热点事件','四月热点事件')

sleep(3)





'''
暂时无法实现拖动功能
#拖动分组
#定位元素的原位置
element=driver.find_element_by_css_selector('[title='+arrgroup[1]+']')
#定位元素要移动到的位置
to_element=driver.find_element_by_css_selector('[title='+arrgroup[0]+']')
#执行拖动
ActionChains(driver).drag_and_drop(element, to_element).perform()
sleep(1)
'''
sleep(3)
driver.quit()