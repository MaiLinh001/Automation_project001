from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.config_reader import ConfigReader

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def load(self):
        self.driver.get(ConfigReader.get_base_url())

    def do_login(self, username, password):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)