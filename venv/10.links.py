import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

#How many links present validate
#capture all links in webpages
#click on the links

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")

links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links presnt:",len(links))

for link in links:
    print(link.text)
driver.find_element(By.LINK_TEXT,"JAVA").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"TES")
time.sleep(10)
driver.close()
