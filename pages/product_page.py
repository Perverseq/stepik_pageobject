from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def should_be_cart_sum_equals_product_price(self, product_price):
        assert self.browser.find_element(*ProductPageLocators.CART_SUM).text == \
               product_price, "Cart sum not equals product price."

    def should_be_message_about_success_adding_to_cart(self, product_name):
        assert f'{product_name} has been added to your basket.' == \
               self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_MESSAGE).text, "Message not show."

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

