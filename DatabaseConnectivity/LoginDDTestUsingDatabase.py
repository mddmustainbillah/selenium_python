import time
from selenium import webdriver
import cx_Oracle
import os
os.environ["PATH"] = "Path of the oracle instant client file"

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
driver.maximize_window()

# Establish connection to the database
con = cx_Oracle.connect('hr','hr', 'localhost/pdborc1')

cur = con.cursor()

query = "select * from users"

cur.execute(query)

for cols in cur:
    driver.find_element_by_name("userName").send_keys(cols[0])
    driver.find_element_by_name("password").send_keys(cols[1])
    driver.find_element_by_name("login").click()
    time.sleep(5)

    # validation started
    if driver.title == "Find a Flight: Mercury Tours:":
        print("Test passed")
    else:
        print("Test failed")
    driver.find_element_by_link_text("Home").click()


cur.close()

con.close()

print("Data Driven Test Completed!!!")
