from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")

driver.implicitly_wait(10)
assert "Welcome: Mercury Tours" in driver.title
print(driver.title)
user=driver.find_element_by_name("userName")
print(user.is_displayed())
print(user.is_enabled())

passwrd=driver.find_element_by_name("password")
print(passwrd.is_displayed())
print(passwrd.is_enabled())

sub=driver.find_element_by_name("submit")
print(sub.is_displayed())
print(sub.is_enabled())

driver.close()