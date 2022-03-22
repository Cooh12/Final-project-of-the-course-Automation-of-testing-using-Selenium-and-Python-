from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def success_add_product(self):
        name_product = self.browser.find_element(By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main h1')
        name_check_product = self.browser.find_element(By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
        assert name_product.text == name_check_product.text, "The names don't match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def add_product_to_basket(self):
        button= self.browser.find_element(*ProductPageLocators.BUTTON_ADD_PRODUCT_TO_BASKET)
        button.click()
        self.solve_quiz_and_get_code()
        self.success_add_product()

    def should_be_basket_page_from_product_page(self):
        self.should_be_basket_page()

    
    



        

