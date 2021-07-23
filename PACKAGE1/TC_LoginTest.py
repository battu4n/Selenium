import unittest
class Logintest(unittest.TestCase):
    def test_loginbyemail(self):
        print("This is login bye email")
        self.assertTrue(True)

    def test_loginbyphone(self):
        print("This is login bye phone")
        self.assertTrue(True)

    def test_loginbytwitter(self):
        print("This is login bye twitter")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()