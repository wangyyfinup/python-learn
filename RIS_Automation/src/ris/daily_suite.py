
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait  
import time

class TestCase:
    def setUp(self):
        self.driver = webdriver.ChromeOptions()
        browser_url = r'C:\Users\Administrator\AppData\Local\360Chrome\Chrome\Application\360chrome.exe'
        self.driver.binary_location = browser_url
        
chromeOptions = webdriver.ChromeOptions()
chromeOptions.binary_location = browser_url
c = webdriver.Chrome(chrome_options = chromeOptions
                     
#driver = webdriver.ChromeOptions()  # 
 
# 打开谷歌浏览器
driver = chromeOptions
driver.get("http://www.youku.com")
 
# 通过q这个属性来找元素 （谷歌搜索框）
inputElement = driver.find_element_by_name("q")
 
# 在搜索框中输入beyond，题外话，beyond是我比较喜欢的乐队，我很喜欢吉他的，正在学呢
inputElement.send_keys("beyond")
 
# 提交搜索信息
inputElement.submit()
 
