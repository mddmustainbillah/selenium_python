# Click on the links

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")

links = driver.find_elements(By.TAG_NAME, "a")



# -------------- How many links present--------------

print("Number of links present:", len(links))  # show how many links present in the page




# -------------------Capture Links-----------------

for link in links:
    print(link.text)



# -------------Clicking on the link (2 methods) ----------------

# method - 1
# driver.find_element(By.LINK_TEXT, "Developers").click() # name have to be 100% correct

# method - 2
driver.find_element(By.PARTIAL_LINK_TEXT, "Develop").click() # name have to be 100% correct