import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()
driver.get("http://demo.guru99.com/test/newtours/")

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()
time.sleep(5)
going=driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[1]/div/div/div/button').send_keys(goa)
returning= driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div[2]/div[1]/div/div[2]/div/div/div/button[1]').send_keys(NYC)
