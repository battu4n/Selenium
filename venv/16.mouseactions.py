import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

user_name = driver.find_element_by_xpath('//*[@id="txtUsername"]').send_keys("Admin")
passwrd = driver.find_element_by_xpath('//*[@id="txtPassword"]').send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

admin=driver.find_element_by_xpath('//*[@id="menu_admin_viewAdminModule"]/b')
usermngmt=driver.find_element_by_xpath('//*[@id="menu_admin_UserManagement"]')
usr= driver.find_element_by_xpath('//*[@id="menu_admin_viewSystemUsers"]')

action = ActionChains(driver)
action.move_to_element(admin).move_to_element(usermngmt).move_to_element(usr).click().perform()

driver.close()