from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCSESSFUL_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info>.alertinner > p > strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info")