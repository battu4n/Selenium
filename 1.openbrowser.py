from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
#driver = webdriver.Ie(executable_path="C:\Program Files\Driver\IEDriverServer.exe")
#driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\gecko.exe")
driver.get("http://www.newtours.demoaut.com/")
print(driver.title)#Tittle of the page
print(driver.current_url)#To return current url
#print(driver.get_screenshot_as_base64())
#print(driver.page_source)
driver.close()
