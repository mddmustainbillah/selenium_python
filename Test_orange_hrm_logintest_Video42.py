#####  Unit Test, POM, HTML Reports   ##########

# Python unittest HTML RestRunner Reports
# Selenium Python test case using Unit Test, HTML Reports
# Selenium Python Project | Unit Test, POM, HTML Reports

# html-testRunner
# ----
# c:/windows/system32>pip install html-testRunner


# Test case: OrangeHRM login test
# ---
# 1) Launch browser
# 2) Verify home page title
# 3) Verify Login
# 4) close browser

#### setUpClass()
#### tearDownClass()

## Command to run unittest test case to generate report:
#-------
# python Test_orange_hrm_logintest_Video42.py


import unittest
import HtmlTestRunner
from selenium import webdriver


class OrangeHRMTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
        cls.driver.maximize_window()

    def test_homePageTitle(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matching.")

    def test_login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com")
        self.driver.find_element_by_name("txtUsername").send_keys("Admin")
        self.driver.find_element_by_name("txtPassword").send_keys("admin123")
        self.driver.find_element_by_name("Submit").click()
        self.assertEqual("OrangeHRM", self.driver.title, "Webpage title is not matching")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print("Test Completed......")


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="Reports"))

