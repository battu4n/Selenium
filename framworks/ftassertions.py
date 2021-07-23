import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testname(self):
        driver=webdriver.Chrome("C:\Program Files\Driver\chromedriver.exe")
        #self.assertIsNone(driver)
        self.assertIsNotNone(driver)

if __name__ == "__main__":
    unittest.main()
