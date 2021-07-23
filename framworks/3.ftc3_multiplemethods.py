import unittest
def setUpModule():
    print("Setup Module")
def teaDownModule():
    print("This is teardown module")
class AppTesting(unittest.TestCase):
    @classmethod
    def setUp(self):
        print("Thsi is login test")
    @classmethod
    def tearDown(self) :
        print("This is logout test ")
    @classmethod
    def setUpClass(cls):
        print("Open an Application")
    @classmethod
    def tearDownClass(cls):
        print("Close application")
    def test_search(self):
        print("This is search test")
    def test_advancedsearch(self):
        print("This is advanced search")
    def test_prepaidrecharge(self):
        print("This is prepaid recharge")
    def test_postppaidreacharge(self):
        print("This is postpiad recharge")
if __name__=="__main__":
    unittest.main()