# performing operation  in every frame
# you have to perform operation one by one. like this sequence
# go first frame and perform  --> back to default content --> then go second frame -->
# again back to default content ......... like this way

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

# ---- first move to one frame -------
driver.switch_to.frame("packageListFrame") # First frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)

# ----- back to the main content ------
driver.switch_to.default_content()

# ------ move to second frame ----
driver.switch_to.frame("packageFrame") # second frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

# ----- back to the main content ------
driver.switch_to.default_content()
time.sleep(3)

# ------ move to third frame ----
driver.switch_to.frame("classFrame") # second frame
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()



