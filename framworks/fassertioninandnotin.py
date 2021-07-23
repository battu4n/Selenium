import unittest

class Test(unittest.TestCase):
    def test_Name(self):
        list={"python","java","perl"}
        self.assertIn("python",list)
    def test_Name1(self):
        list1={"python",".Net","perl"}
        self.assertNotIn("selenium",list1)
if __name__ == "__main__":
    unittest.main()