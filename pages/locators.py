from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '[id="login_link"]')
    BASKET_LINK = (By.CSS_SELECTOR, '#default > header > div.navbar.primary.navbar-static-top.navbar-inverse > div > div.navbar-collapse.primary-collapse.collapse > form > input')
    BASKET_IS_EMPTY = (By.CLASS_NAME, 'basket-items')
    TEXT_THAT_THE_BASKET_IS_EMPTY = (By.ID, 'content_inner')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user") 

class LoginPageLocators():
    LOGIN_URL = (By.ID, 'login_link')
    LOGIN_FORM = (By.ID, "login_form")
    REGISTRATION_FORM = (By.ID, "register_form")
    REGISTRATION_INPUT_EMAIL = (By.ID, 'id_registration-email')
    REGISTRATION_INPUT_PASSWORD_1 = (By.ID, 'id_registration-password1')
    REGISTRATION_INPUT_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTRATION_BUTTON = (By.XPATH, '/html/body/div[2]/div/div[2]/div[2]/div/div[2]/form/button')
    REGISTRATION_SUCCSESS = (By.XPATH,'/html/body/div[2]/div/div/div/div[1]/div/div')

class ProductPageLocators():
    BUTTON_ADD_PRODUCT_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    TABLE_PRODUCT_INFO = (By.CLASS_NAME,'table-striped')
    PRODUCT_NAME = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main h1')
    PRODUCT_NAME_AFTER_ADDING = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[2]/div/strong[contains(text(), "Deferred benefit offer")]')
    NAME_PRODUCT = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main h1')
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div > strong')