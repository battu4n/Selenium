import XLutils
from selenium import webdriver
import logging

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.maximize_window()

driver.get("http://demo.guru99.com/test/newtours/")
driver.maximize_window()

path = "C:/Users/marut/Downloads/empty.xlsx"

rows=XLutils.getRowCount(path,'Sheet1')

for r in range(2,rows+1):
    Username=XLutils.readData(path,"Sheet1",r,1)
    Password=XLutils.readData(path,"Sheet1",r,2)

    driver.find_element_by_name("userName").send_keys(Username)
    driver.find_element_by_name("password").send_keys(Password)
    driver.find_element_by_name("submit").click()
    print(driver.title)
    if driver.title=="Welcome: Mercury Tours":
        print(("test is passed"))
        XLutils.writeData(path,'Sheet1',r,3,"test passed")
    else:
        print("test failed")
        XLutils.writeData(path,'Sheet1',r,3,"test failed")
    driver.find_element_by_link_text("Home").click()
logging.basicConfig(filename="D:/screenshots/test.log",format='%(asctime)s:%(levelname)s:%(message)s',level=logging.DEBUG)
driver.quit()