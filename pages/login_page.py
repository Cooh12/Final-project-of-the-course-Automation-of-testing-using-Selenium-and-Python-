import time
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

    def register_new_user(self):
        email = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_EMAIL)
        email.send_keys(str(time.time()) + "@fakemail.org")
        password_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_1)
        password_1.send_keys('eRk-2D7-KNt-XGY')
        password_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_INPUT_PASSWORD_2)
        password_2.send_keys('eRk-2D7-KNt-XGY')
        registration_button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        registration_button.click()
        self.should_be_succsess_registration()
        self.should_be_authorized_user()

    def should_be_succsess_registration(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTRATION_SUCCSESS), "There is no message about successful registration"

    def should_be_register_form(self):
        register_form = self.browser.find_element(*LoginPageLocators.REGISTRATION_FORM)
        assert register_form, "Register form is not presented"