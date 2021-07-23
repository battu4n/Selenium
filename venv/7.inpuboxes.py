import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#How to find how many input boxes present in webpage
inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputboxes))


#How to provide values into text box

first_name= driver.find_element(By.ID,"RESULT_TextField-1").send_keys("Battu")
time.sleep(10)
last_name = driver.find_element(By.ID,'RESULT_TextField-2').send_keys("Narendra")
time.sleep(5)
phone= driver.find_element_by_id('RESULT_TextField-3').send_keys("9556633887")
print(phone)
driver.close()

