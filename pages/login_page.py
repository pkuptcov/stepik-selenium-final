from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_CONFIRM_INPUT)
        login_submit = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        email_input.send_keys(email)
        password_input.send_keys(password)
        password_confirm_input.send_keys(password)
        login_submit.click()

    def auth_user(self, email, password):
        email_input = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL_INPUT)
        password_input = self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD_INPUT)
        login_submit = self.browser.find_element(*LoginPageLocators.LOGIN_SUBMIT)
        email_input.send_keys(email)
        password_input.send_keys(password)
        login_submit.click()