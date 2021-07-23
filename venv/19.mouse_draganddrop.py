import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


source = driver.find_element_by_xpath('//*[@id="box6"]')
source1=driver.find_element_by_xpath('//*[@id="box3"]')
destination1=driver.find_element_by_xpath('//*[@id="box103"]')

destination= driver.find_element_by_xpath('//*[@id="box106"]')


actions = ActionChains(driver)

actions.drag_and_drop(source,destination).perform()
actions.drag_and_drop(source1,destination1).perform()
time.sleep(5)
driver.close()