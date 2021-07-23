import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testname(self):
        driver = webdriver.Chrome("C:\Program Files\Driver\chromedriver.exe")
        driver.get("https://google.com")
        tittleofwebpage = driver.title
        #asserequal
        #self.assertEqual("Google",tittleofwebpage,"webpage tittle is not same")
        self.assertNotEqual("Gogle", tittleofwebpage, "webpage tittle is not same")

if __name__=="__main__":
    unittest.main()