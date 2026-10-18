from selenium.webdriver.common.by import By

from pages1.basepage1 import Basepage


class LoginPage(Basepage):
    USERNAME = (By.XPATH,"//input[@placeholder='Username']")
    PASSWORD = (By.XPATH,"//input[@placeholder='Password']")
    LOGIN = (By.XPATH,"//button[@type='submit']")
    ERROR_MESSAGE = (By.CSS_SELECTOR,".oxd-text.oxd-text--p.oxd-alert-content-text")

    def open_login(self):
        self.open_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


    def enter_credentials(self,username,password):
        self.enter_text(self.USERNAME,username)
        self.enter_text(self.PASSWORD,password)

    def signin(self):
        self.click_element(self.LOGIN)

    def invalid_login(self):
        return self.get_text(self.ERROR_MESSAGE)






