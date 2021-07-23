import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
#driver = webdriver.Ie(executable_path="C:\Program Files\Driver\IEDriverServer.exe")
#driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\gecko.exe")

driver.get("http://demo.guru99.com/test/newtours/")#FR Application
print(driver.title)
driver.get("http://pavantestingtools.blogspot.in/")#Testing
print(driver.title)
time.sleep(5)
driver.back()
print(driver.title)
time.sleep(5)
driver.forward()
print(driver.title)
driver.close()

