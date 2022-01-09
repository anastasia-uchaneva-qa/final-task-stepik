from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def should_be_successful_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), "Successful message after adding book is not presented"

    def should_not_be_successful_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_dissappeared_successful_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESSFUL_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_message_with_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRICE), "Message with price after adding book is not presented"

    def check_name_of_book(self):
        name_of_book = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK).text
        name_of_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_OF_BOOK_IN_BASKET).text
        assert name_of_book == name_of_book_in_basket, "Name of the book is not the same!"

    def check_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE).text
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price == price_in_basket, "Price of the book is not the same"
