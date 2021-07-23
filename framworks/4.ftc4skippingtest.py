import unittest

class AppTesting(unittest.TestCase):
    @unittest.SkipTest
    def test_search(self):
        print("This is your search test")
    def test_advancedsearch(self):
        print("this is advanced seach")
    def test_prepaidreacharge(self):
        print("Thsi is prepaid recharge")
    def test_postpaid(self):
        print("This is postpaid reacharge")
    def test_logingbygmail(self):
        print("This is logging by gmail")
    @unittest.skip("i am skipping this because of no need to run")
    def test_loggingbyfb(self):
        print("This is logging by fb")

if__name__="__main__"
unittest.main()
