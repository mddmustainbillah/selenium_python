from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.google.com/")

# driver.save_screenshot("C:/Users/Titan Tech-2/PycharmProjects/SeleniumWithPython/output/google.png")


driver.get_screenshot_as_file("C:/Users/Titan Tech-2/PycharmProjects/SeleniumWithPython/output/google2.png")

# Note: png, jpg, jpeg etc any extension applicable