from selenium.webdriver.common.by import By
from Pages.base_page import Basepage


class LoginPage(Basepage):
    EMAIL = (By.ID,":r1:")
    PASSWORD = (By.ID,":r2:")
    signin = (By.XPATH,"//button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH,"//p[text()='*Invalid email!']")

    def open_login_page(self):
        self.open_url("https://v2.zenclass.in/login")

    def check_email_box(self):
        self.element_displayed_enabled(self.EMAIL)

    def check_password_box(self):
        self.element_displayed_enabled(self.PASSWORD)

    def check_signin_button(self):
        self.element_displayed_enabled(self.signin)

    def login(self,email,password):
        self.enter_text(self.EMAIL,email)
        self.enter_text(self.PASSWORD,password)
        self.click(self.signin)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)
