import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

radio_button = driver.find_elements_by_class_name('multiple_choice')
print(len(radio_button))

status = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(status)

driver.find_element(By.ID,"RESULT_RadioButton-7_0").click()

driver.close()