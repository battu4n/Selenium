import unittest
from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome("C:\Program Files\Driver\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Tittle of the page is:",self.driver.title)
        self.driver.close()
    def test_bing(self):
        self.driver=webdriver.Chrome("C:\Program Files\Driver\chromedriver.exe")
        self.driver.get("https://bing.com")
        print("Tittle of the bing search is:",self.driver.title)
        self.driver.close()
if __name__=="__main__":
    unittest.main()