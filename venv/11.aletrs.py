import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()


driver.get("https://testautomationpractice.blogspot.com/")

clickme= driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()
time.sleep(5)

#driver.switch_to_alert().accept()#To close by using ok button

#to discard popup window

driver.switch_to_alert().dismiss()#To dismiss alert box

driver.close()
