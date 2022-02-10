from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://testautomationpractice.blogspot.com/")

rows = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr")) # count number of rows
cols = len(driver.find_elements_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr[1]/th")) # count number of columns

print(rows)
print(cols)

print("BookName" + "        " + "Author" + "          " + "Subject" + "        " + "Price")

for i in range(2, rows+1):
    for j in range(1, cols+1):
        value = driver.find_element_by_xpath("//*[@id='HTML1']/div[1]/table/tbody/tr["+str(i)+"]/td["+str(j)+"]").text
        print(value, end="        ")
    print()

