import unittest
class Signuptest(unittest.TestCase):
    def test_signupbyemail(self):
        print("This is signup by email")
        self.assertTrue(True)

    def test_signupbyphone(self):
        print("This is signup by phone")
        self.assertTrue(True)

    def test_signupbytwitter(self):
        print("This is signup by twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()