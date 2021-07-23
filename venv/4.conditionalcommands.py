from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver= webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")

user=driver.find_element_by_name("userName")
print(user.is_displayed())
print(user.is_enabled())

passwrd=driver.find_element_by_name("password")
print(passwrd.is_displayed())
print(passwrd.is_enabled())

sub=driver.find_element_by_name("submit")
print(sub.is_displayed())
print(sub.is_enabled())


user.send_keys("mercury")
passwrd.send_keys("mercury")
sub.click()
print(driver.title)
flights= driver.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td[1]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/a').click()
driver.close()