from selenium.webdriver.ie.options import Options  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
 
__browser_url = r'C:\Users\editor07.EDITOR07\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址
ie_options = Options()
ie_options.INITIAL_BROWSER_URL= __browser_url

#driver = webdriver.Ie()

#driver.get('http://www.baidu.com')  
#driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)  
#time.sleep(30)  
#driver.quit()