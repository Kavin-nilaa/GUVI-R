from selenium.webdriver.common.by import By
from pages1.basepage1 import Basepage


class HomePage(Basepage):
    DASHBOARD= (By.XPATH,"//h6[text()='Dashboard']")
    DROPDOWN = (By.CLASS_NAME,"oxd-userdropdown-name")
    LOGOUT = (By.XPATH,"//a[text()='Logout']")

    def verify_login(self):
        actual = self.get_text(self.DASHBOARD)
        assert actual == "Dashboard"

    def Logout_Page(self):
        self.click_element(self.DROPDOWN)
        self.click_element(self.LOGOUT)

    def close(self):
        self.close_browser()



