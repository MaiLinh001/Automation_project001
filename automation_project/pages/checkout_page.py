from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    CONFIRMATION_HEADER = (By.CLASS_NAME, "complete-header")
    CONFIRMATION_BODY = (By.CLASS_NAME, "complete-text")
    
    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_text(self.FIRST_NAME, first_name)
        self.enter_text(self.LAST_NAME, last_name)
        self.enter_text(self.ZIP_CODE, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_order(self):
        self.click(self.FINISH_BUTTON)

    def get_confirmation_message(self):
        header = self.get_text(self.CONFIRMATION_HEADER)
        body = self.get_text(self.CONFIRMATION_BODY)
        return header, body
    