class LoginPage():
    # Locators of all the elements
    textbox_username_id = "//*[@id='Email']"
    textbox_password_id = "//*[@id='Password']"
    button_login_xpath = "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    # link_logout_linkText = "wellcome"
    link_logout_linktext = "//*[@id='navbarText']/ul/li[3]/a"

    def __init__(self, driver):   # Constructor
        self.driver = driver

    # def setUserName(self, username):
    #     self.driver.find_element_by_xpath(self.textbox_username_id).send_keys(username)
    #
    # def setPassword(self, password):
    #     self.driver.find_element_by_xpath(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_linktext).click()