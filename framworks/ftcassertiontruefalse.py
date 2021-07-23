import unittest
from selenium import webdriver

class Test(unittest.TestCase):
     def test_Name(self):
        driver = webdriver.Chrome("C:\Program Files\Driver\chromedriver.exe")
        driver.get("https://google.com")
        tittleofwebpage=driver.title
        self.assertTrue(tittleofwebpage == "Google")
        print("This is pass")
if __name__=="__main__":
    unittest.main()