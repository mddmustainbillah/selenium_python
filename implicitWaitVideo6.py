from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://facebook.com")
# print(driver.title)

driver.implicitly_wait(10)

assert "Facebook – log in or sign up" in driver.title

driver.find_element_by_name("email").send_keys("dfsfhsdkjfh")
driver.find_element_by_name("pass").send_keys("dsfhdsf")

driver.find_element_by_name("login").click()




