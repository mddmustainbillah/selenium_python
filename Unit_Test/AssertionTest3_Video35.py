######### assertIsNone & assertIsNotNone ##############

##### assertIsNone
# assertIsNone method varifies whether give values of expression results in None or not,
# if the result is none then python unittest will pass the test case otherwise fails the
# testcase.

######## assertIsNotNone
# assertIsNOtNone method verifies whether give values is not Not, if the value is None then
# the test case will be failed.


import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        # driver = None
        #
        # self.assertIsNone(driver)
        self.assertIsNotNone(driver)


if __name__ == "__main__":
    unittest.main()