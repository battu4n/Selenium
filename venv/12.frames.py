import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?org/openqa/selenium/firefox/package-summary.html")

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("org.openqa.selenium.io").click()

driver.switch_to_default_content()

driver.switch_to_frame("classFrame")
driver.find_element_by_link_text("Action").click()

driver.switch_to_default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath('/html/body/header/nav/div[1]/div[1]/ul/li[6]/a').click()
driver.close()