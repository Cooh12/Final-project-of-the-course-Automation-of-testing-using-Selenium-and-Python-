from .base_page import BasePage
from .locators import  LoginPageLocators

from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        assert login_url, "Login url is not presented"

    def should_be_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        assert login_form, "Login from is not presented"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        assert register_form, "Register form is not presented"