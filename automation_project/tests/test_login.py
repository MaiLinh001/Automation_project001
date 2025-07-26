import pytest
from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader
from time import sleep
import allure

@pytest.mark.usefixtures("setup")
class TestLogin(BaseTest):

    @allure.story("Valid Login")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_login(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())
        sleep(5)
        assert "inventory" in self.driver.current_url
