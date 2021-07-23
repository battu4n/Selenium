import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

#how to select 1 option
#How many options exist

element= driver.find_element_by_id("RESULT_RadioButton-9")
drp=Select(element)
#Select by visible text
#drp.select_by_visible_text('Morning')
#select by index
#drp.select_by_index('2')
#Select by value
drp.select_by_value("Radio-2")

#capture all options and print them

#count number of options

print(len(drp.options))

all_options = drp.options
for option in all_options:
    print(option.text)

driver.close()
