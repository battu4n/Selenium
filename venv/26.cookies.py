from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Program Files\Driver\chromedriver.exe")
driver.get("https://www.amazon.in")


#Capture all cokies from amazon

cookies= driver.get_cookies()
print(len(cookies))

print(cookies)#Prill all coocki pairs

#Adding new cookie to browser
cookie = {'name':'MyCookie','value':'12345'}
driver.add_cookie(cookie)
cookies= driver.get_cookies()
print(len(cookies))

print(cookies)

#How to delete cookie

driver.delete_cookie('MyCookie')
cookies= driver.get_cookies()
print(len(cookies))

print(cookies)
#To delete all cookies
driver.delete_all_cookies()
cookies= driver.get_cookies()
print(len(cookies))

print(cookies)

driver.close()