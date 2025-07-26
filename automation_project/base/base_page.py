"""base_page.py: contains common reusable methods such as find_element, click, send_keys, and wait_for_element using WebDriverWait."""
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from utils.config_reader import ConfigReader

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = ConfigReader.get_implicit_timeout()

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        element = self.wait_for_element_clickable(locator)
        try:
            element.click()
        except StaleElementReferenceException:
            self.wait_for_element_clickable(locator).click()

    def enter_text(self, locator, text, clear_first=True):
        element = self.wait_for_element_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def wait_for_element_clickable(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def get_text(self, locator):
        return self.wait_for_element_visible(locator).text
