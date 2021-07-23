import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
#driver = webdriver.Ie(executable_path="C:\Program Files\Driver\IEDriverServer.exe")
#driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\gecko.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)
driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()
time.sleep(5)
#driver.close()
driver.quit()