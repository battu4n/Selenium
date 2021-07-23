import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element_by_xpath('//*[@id="Tabbed"]/a/button').click()

print(driver.current_window_handle)#To get currwnt window values
print(driver.window_handles)#To get all window handlw values
driver.quit()