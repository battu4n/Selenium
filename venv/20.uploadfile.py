import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

driver.switch_to_frame(0)

driver.find_element_by_xpath('//*[@id="RESULT_FileUpload-10"]').send_keys("C:\Users\marut\Desktop\Capture.PNG")