from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_BLOCK), \
            "Products should not be, but they are"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "Empty basket message is not presented, but should be"


