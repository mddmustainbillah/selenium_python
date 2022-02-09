import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# How to find out how many inputboxes present in web page
inputboxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(inputboxes))   # 6

# How to provide value into input boxes
driver.find_element(By.ID, "RESULT_TextField-1").send_keys("Mustain")
driver.find_element(By.ID, "RESULT_TextField-2").send_keys("Billah")
driver.find_element(By.ID, "RESULT_TextField-3").send_keys("4587357")

# How to get the status
status = driver.find_element(By.ID, "RESULT_TextField-3").is_displayed()
print("Displayed or not: ", status)

status = driver.find_element(By.ID, "RESULT_TextField-3").is_enabled()
print("Enabled or not", status)

time.sleep(5)


driver.close()