import unittest
import HtmlTestRunner
from selenium import webdriver
import sys
import time

# import sys.path.append("C://Users/Titan Tech-2/PycharmProjects/SeleniumWithPython/PythonUnitTestProject_POMBased")

from PythonUnitTestProject_POMBased.pageObjects.LoginPage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL = "http://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    def test_login(self):
        lp = LoginPage(self.driver)
        # lp.setUserName(self.username)
        # lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        self.assertEqual("Dashboard / nopCommerce administration", self.driver.title, "Webpage title is not matched")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="../reports"))
