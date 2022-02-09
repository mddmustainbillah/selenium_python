from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

element = driver.find_element_by_id("RESULT_RadioButton-9")
drp = Select(element)

# ----- select one option (3 methods)-----

# Select by visible text
drp.select_by_visible_text("Morning") # Morning
# # Select by index
# drp.select_by_index(2) # Afternoon
# # select by value
# drp.select_by_value("Radio-2") # Evening


# --------Count number of options----------
print(len(drp.options))


# ------ Capture all the options and print them as output ----------
all_options = drp.options
for option in all_options:
    print(option.text)








