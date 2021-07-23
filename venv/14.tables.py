import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.seleniumeasy.com/test/table-pagination-demo.html")
rows= driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/table/thead/tr")
column = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/section/div/table/thead/tr/th")

print(rows)
print(column)
