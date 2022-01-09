from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    MESSAGE_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner>p")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    CONFIRM_PASSWORD_REGISTER_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//*[@name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESSFUL_MESSAGE = (By.CSS_SELECTOR, ".alert-success:first-child")
    NAME_OF_BOOK = (By.CSS_SELECTOR, ".product_main > h1")
    NAME_OF_BOOK_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > strong")
    PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info>.alertinner > p > strong")
    MESSAGE_WITH_PRICE = (By.CSS_SELECTOR, ".alert-info")
