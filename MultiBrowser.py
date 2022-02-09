from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# s = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver = webdriver.Firefox(executable_path="C:\Drivers\geckodriver-v0.30.0-win64\geckodriver.exe")
# driver = webdriver.Ie(executable_path="C:\Drivers\IEDriverServer_Win32_4.0.0\IEDriverServer.exe")


driver.get("http://apple.com")
print(driver.title) # Title of the page
print(driver.current_url) # returns the url of the page
# print(driver.page_source) #HTML

driver.close()  # Close the browser




# Note:

# It will give this error if do not import service and work with service

# C:\Users\Titan Tech-2\PycharmProjects\SeleniumWithPython\MultiBrowser.py:8:
# DeprecationWarning: executable_path has been deprecated, please pass in a Service object
#   driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")


# Solution:
# s = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Chrome(service=s)