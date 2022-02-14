############### Data Driven Test Case ################
# Objectives: 1. Read data from excel
#               2. And write data into excel

##### Common activities for all DDT Case
#   1. Find how many rows
#   2. Find how many columns
#   3. Read data
#   4. Write data           NOTE: create a separate module for common activities

import XLUtils
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com")
driver.maximize_window()

path = "C:/Users/Titan Tech-2/PycharmProjects/SeleniumWithPython/Data Driven Test/DDLC.xlsx"

rows = XLUtils.getRowCount(path, "Sheet1")

for r in range(2, rows+1):
    username = XLUtils.readData(path, "Sheet1", r, 1)
    password = XLUtils.readData(path, "Sheet1", r, 2)

    driver.find_element_by_xpath("").send_keys(username)
    driver.find_element_by_xpath("").send_keys(password)

    driver.find_element_by_xpath("").click()

    if driver.title == " ":
        print("test is passed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Passed")
    else:
        print("Test failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "Test Failed")

    driver.find_element_by_link_text("Home").click()  # Back again to login page

















