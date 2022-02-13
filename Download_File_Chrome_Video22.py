from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Specify the download path
# chromeOptions = Options()
# chromeOptions.add_experimental_option("prefs", {"download.default_directory": "C:\Users\Titan Tech-2\Downloads"})
# driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe",
#                           chrome_options=chromeOptions)

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")

driver.maximize_window()

# Download the txt file
# driver.find_element_by_id("textbox").send_keys("Testing download txt file")
# driver.find_element_by_xpath("//*[@id='createTxt']").click()  # Generate file button
# driver.find_element_by_id("link-to-download").click()  # Download link

# Download pdf file
driver.find_element_by_id("textbox").send_keys("Testing download pdf file")
driver.find_element_by_xpath("//*[@id='createTxt']").click()  # Generate file button
driver.find_element_by_id("link-to-download").click()  # Download link

# Download pdf file
driver.find_element_by_id("pdfbox").send_keys("Testing download pdf file")
driver.find_element_by_id("createPdf").click()  # Generate file button
driver.find_element_by_id("pdf-link-to-download").click()  # Download link
