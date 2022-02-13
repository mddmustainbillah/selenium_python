from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.maximize_window()

driver.switch_to_frame(0)

driver.find_element_by_xpath("//*[@id='RESULT_FileUpload-10']").send_keys("C:/Users/Titan Tech-2/Pictures/flower.jpg")