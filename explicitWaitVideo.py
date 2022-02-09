from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")

driver.find_element(By.XPATH, "//*[@id='wizardMainRegionV2']/div/div/div/div/ul/li[2]/a/span").click()  # flight button
# driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/div[1]/button").click() # origin
driver.find_element(By.XPATH, "//*[@id='location-field-leg1-origin-menu']/div[1]/div[1]/button").send_kSeys("SFO")# origin
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='wizard-flight-tab-roundtrip']/div[2]/div[1]/div/div[2]/div/input").send_keys(
    "NYC")  # destination

driver.find_element(By.ID, "d1").clear()
driver.find_element(By.ID, "d1").send_keys("Feb 21")

driver.find_element(By.ID, "d2-btn").clear()
driver.find_element(By.ID, "d2-btn").send_keys("Feb 23")

driver.find_element(By.XPATH, "//*[@id='wizard-flight-pwa-1']/div[3]/div[2]/button").click()

# Explicit waits
wait = WebDriverWait(driver, 10) # waits maximum 10 sec if elements not found. If found then without waiting go next
element = wait.until(EC.element_to_be_clickable(By.XPATH, ""))
element.click()

time.sleep(3)

driver.quit()







