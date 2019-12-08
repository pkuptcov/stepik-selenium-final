from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocator.ADD_TO_BASKET_BUTTON)
        add_to_cart_button.click()

    def should_be_right_title(self):
        product_title = self.browser.find_element(*ProductPageLocator.PRODUCT_TITLE).text
        success_message = self.browser.find_element(*ProductPageLocator.SUCCESS_MESSAGE).text
        assert f'{product_title} был добавлен в вашу корзину.' == success_message, "Product title doesn't match product name added"

    def should_be_right_price(self):
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE).text
        basket_total = self.browser.find_element(*ProductPageLocator.BASKET_TOTAL).text
        assert product_price in basket_total, "Product price isn't equal to basket price"