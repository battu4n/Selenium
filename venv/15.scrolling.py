import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

#we can scroll page by 3 types pixels,elemts and bottom

driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
#scroll by using pixel number

driver.execute_script("window.scrollBy(0,1000)","")

#scroll by using element

"""driver.execute_script(driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div/div/div[79]/div/a/img"))
driver.execute_script("arguments[0].scrollIntoView();",flag)"""

#scroll the till end of the page

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

driver.close()