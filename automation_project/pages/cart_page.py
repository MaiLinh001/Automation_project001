from selenium.webdriver.common.by import By
from base.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)