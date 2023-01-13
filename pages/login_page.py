from .base_page import BasePage
from .locators import LoginFormLocators, UserRegistrationFormLocators 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random


class LoginPage(BasePage):
    def should_be_login_page(self):

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        corrent_url = self.browser.current_url
        assert "login" in corrent_url, "not is login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginFormLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginFormLocators.REGISTER_FORM), "Register form is not present"

    def registe_new_user(self):

        email = f'name{str(time.time())}@fakemail.com'
        password = f'qwe{random.randint(1, 999)}asd{random.randint(1, 999)}QAZ'

        reg_email_address_form = self.browser.find_element(*UserRegistrationFormLocators.REGISTRATION_EMAIL_ADDRESS_FORM)
        reg_email_address_form.send_keys(email)
        reg_password_form = self.browser.find_element(*UserRegistrationFormLocators.REGISTRATION_PASSWORD_FORM)
        reg_password_form.send_keys(password)
        reg_confirm_password_form = self.browser.find_element(*UserRegistrationFormLocators.REGISTRATION_CONFIRM_PASSWORD_FORM)
        reg_confirm_password_form.send_keys(password)
        button_registration_form = self.browser.find_element(*UserRegistrationFormLocators.BUTTON_REGISTRATION_FORM)
        button_registration_form.click()



        








