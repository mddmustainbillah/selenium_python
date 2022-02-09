from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.facebook.com/")

user_ele = driver.find_element_by_name("email")
print(user_ele.is_displayed()) # returns true/false based of element status
print(user_ele.is_enabled()) # returns true/false

pwd_ele = driver.find_element_by_name("pass")
print(pwd_ele.is_displayed())
print(pwd_ele.is_enabled())

user_ele.send_keys("username")  # type username for login
pwd_ele.send_keys("password")   # type password for login

driver.find_element_by_name("login").click()   # click the login button

roundtrip_radio = driver.find_element_by_css_selector("input[value=roundtrip]") # Here, input is css tag and value=roundtrip is css selector
print("Status of round trip radio button", roundtrip_radio.is_selected()) # return true/false status

onetrip_radio = driver.find_element_by_css_selector("input[value=oneway]")
print("Status of oneway radio button", onetrip_radio.is_selected())























