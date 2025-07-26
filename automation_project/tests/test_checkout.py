from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config_reader import ConfigReader
from time import sleep
import allure

class TestCheckout(BaseTest):

    @allure.story("Complete checkout with valid info")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_products_and_checkout(self):
        login_page = LoginPage(self.driver)
        login_page.load()
        login_page.do_login(ConfigReader.get_username(), ConfigReader.get_password())

        inventory_page = InventoryPage(self.driver)
        inventory_page.add_first_n_items_to_cart(3)
        inventory_page.go_to_cart()
        sleep(2)

        cart_page = CartPage(self.driver)
        cart_page.click_checkout()
        sleep(2)

        checkout_page = CheckoutPage(self.driver)
        checkout_page.fill_checkout_form("John", "Doe", "70000")
        checkout_page.finish_order()
        sleep(2)

        header, body = checkout_page.get_confirmation_message()
        assert header == "Thank you for your order!", f"Expected header not found: {header}"
        assert body == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", f"Expected body not found: {body}"
       