# Cookie is a piece of information from website and saved by your web browser
# cookies are a way to remembering users and their interaction with the site by
#     storing information in the cookie file as key value pairs.
# It stores the login information like user name/email and password
# HTTP cookie is also known as a web cookie, a browser cookie or Internet cookie

# ###### Operations on Cookies #####
# 1. Capture all cookies from browser
# 2. Count number of cookies
# 3. Read Cookie pairs
# 4. Adding new cookies
# 5. Deleting spwcific cookies by using name of cookie
# 6. Deleting all the cookies

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.amazon.in/")

# Capture all the cookies created by browser
cookies = driver.get_cookies()
print(len(cookies)) # number of the cookies
print(cookies)  # Print all the cookies pair

# Adding new cookie to the browser
cookie = {'name':'Mycookie', 'value': '12335364642'}
driver.add_cookie(cookie)

cookies = driver.get_cookies()
print(len(cookies)) # number of the cookies after adding new cookie
print(cookies)  # Print all the cookies pair

# Deleting cookie
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print(len(cookies))  # Print number of cookies after deleting the cookie

# Deleting all the cookie
driver.delete_all_cookies() # deletes all cookies
cookies = driver.get_cookies() # capture all the cookies after deletes all
print(len(cookies))     # 0









