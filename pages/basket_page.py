from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items are presented, but should not be"

    def should_be_message_empty_basket(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_EMPTY_BASKET), "Message about empty basket is not presented"
