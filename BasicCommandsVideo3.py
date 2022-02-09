from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# chrome
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) # returns the title of the browser
print(driver.current_url) # returns url of the page

# Click on a button
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)


# driver.close()  # close one tab/browser at a time

driver.quit()   # close all the tabs/browser