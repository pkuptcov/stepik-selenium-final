from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocator:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@type='submit'][@class='btn btn-lg btn-primary btn-add-to-basket']")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]")
    PRODUCT_TITLE = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_TOTAL = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")