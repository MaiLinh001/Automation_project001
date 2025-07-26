"""base_test.py: handles setup/teardown using pytest fixtures."""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.config_reader import ConfigReader
import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        #Setup
        s = Service(executable_path="D:\\chromedriver-win64\\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)
        self.driver.maximize_window()
        self.driver.implicitly_wait(ConfigReader.get_implicit_timeout())
        self.driver.set_page_load_timeout(ConfigReader.get_page_load_timeout())
        self.driver.get(ConfigReader.get_base_url())
        request.cls.driver = self.driver

        yield

        # Teardown
        self.driver.quit()