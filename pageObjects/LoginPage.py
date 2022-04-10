from  selenium import webdriver
class Login:
    textbox_Email_id='ap_email'
    button_continue_xpath="//input[@id='continue']"
    textbox_password_id="ap_password"
    button_login_xpath="//input[@id='signInSubmit']"
    link_signout_linktext="Sign Out"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_Email_id).clear()
        self.driver.find_element_by_id(self.textbox_Email_id).send_keys(username)

    def clickcountinue(self):
        self.driver.find_element_by_xpath(self.button_continue_xpath).click()

    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.link_signout_linktext).click()



