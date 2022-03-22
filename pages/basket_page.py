from pages.base_page import BasePage
from pages.locators import ProductPageLocators

from .locators import MainPageLocators
class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.go_to_basket_page()
        self.should_not_be_basket_is_empty()
        self.should_text_that_the_basket_is_empty()

    def go_to_basket_page(self):
        login_link = self.browser.find_element(*MainPageLocators.BASKET_LINK)
        login_link.click() 
    
    def should_not_be_basket_is_empty(self):
        basket_items = self.is_not_element_present(*MainPageLocators.BASKET_IS_EMPTY)

    def should_text_that_the_basket_is_empty(self):
        text_basket_is_empty = self.is_element_present(*MainPageLocators.TEXT_THAT_THE_BASKET_IS_EMPTY)