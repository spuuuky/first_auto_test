from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginFormLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductBascetLocators():
    TEXT_PRODUCT = (By.TAG_NAME, "h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, "p.price_color")
    ADD_BASCET = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")
    BASCET_TEXT_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    BASCET_PRICE_PRODUCT = (By.CSS_SELECTOR, ".alertinner p strong")

class ProductPageLocators():
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alertinner")

class BasePageLocators():
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")   ## попросили добавить по курсу
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BascetPageLocators():
    BASCET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    BASCET_TEXT = (By.CSS_SELECTOR, "#content_inner p")

class UserRegistrationFormLocators():
    REGISTRATION_EMAIL_ADDRESS_FORM = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_FORM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION_FORM = (By.NAME, "registration_submit")
