from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")

driver.get("http://demo.guru99.com/test/newtours/index.php")
#driver.save_screenshot("D:\screenshots\homepage.png")

driver.get_screenshot_as_file("D:\screenshots\homepage1.png")

driver.close()