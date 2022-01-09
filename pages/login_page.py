from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        email_register_input = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTER_INPUT)
        password_register_input = self.browser.find_element(*LoginPageLocators.PASSWORD_REGISTER_INPUT)
        confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_REGISTER_INPUT)
        button_register = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        email_register_input.send_keys(email)
        password_register_input.send_keys(password)
        confirm_password_input.send_keys(password)
        button_register.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"
