from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://google.com/")
print(driver.title)

driver.get("http://apple.com/")
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)
time.sleep(5)


driver.forward()
time.sleep(5)
print(driver.title)

driver.close()
