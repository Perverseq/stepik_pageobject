from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    CART_SUM = (By.CSS_SELECTOR, 'div.alertinner > p:nth-child(1) > strong')
    ADDED_TO_CART_MESSAGE = (By.CSS_SELECTOR, '#messages > div:nth-child(1) > div')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
