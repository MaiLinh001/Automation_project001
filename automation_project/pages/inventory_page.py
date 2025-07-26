from selenium.webdriver.common.by import By
from base.base_page import BasePage

class InventoryPage(BasePage):
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_first_n_items_to_cart(self, count):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BUTTONS)
        for btn in buttons[:count]:
            btn.click()

    def go_to_cart(self):
        self.click(self.CART_ICON)