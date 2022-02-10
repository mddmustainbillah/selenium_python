from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

driver.find_element(By.XPATH, """//*[@id="Tabbed"]/a/button""").click()

print(driver.current_window_handle) # Return the parent window handle value

handles = driver.window_handles # returns all the handle values of opened browser windows

for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title == "Frames & windows":
        driver.close()

driver.quit()