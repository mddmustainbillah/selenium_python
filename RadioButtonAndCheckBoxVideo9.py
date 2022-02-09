import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

s = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
driver = webdriver.Chrome(service=s)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# # Working with the radio button
# status = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()  # show false
# print(status)
#

driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label").click() # click method select radio button
#
# status2 = driver.find_element(By.ID, "RESULT_RadioButton-7_0").is_selected()  # show false
# print(status2)

# Working with check boxes
# driver.find_element_by_id("RESULT_CheckBox-8_0").click()
# driver.find_element_by_id("RESULT_CheckBox-8_5").click()
driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[1]/td/label" ).click()


















