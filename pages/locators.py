from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_CONFIRM_INPUT = (By.ID, "id_registration-password2")
    REGISTER_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocator:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[@type='submit'][@class='btn btn-lg btn-primary btn-add-to-basket']")
    SUCCESS_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]")
    PRODUCT_TITLE = (By.XPATH, "//h1")
    PRODUCT_PRICE = (By.XPATH, "//p[@class='price_color']")
    BASKET_TOTAL = (By.XPATH, "//div[@class='basket-mini pull-right hidden-xs']")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_BLOCK = (By.XPATH, "//*[@id='basket_formset']/div")
    BASKET_IS_EMPTY = (By.XPATH, "//*[@id='content_inner']")