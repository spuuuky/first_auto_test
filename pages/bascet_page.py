from .locators import BascetPageLocators
from .base_page import BasePage

class BascetPage(BasePage):
    def bascet_text_true(self):
        text_page = self.browser.find_element(*BascetPageLocators.BASCET_TEXT)
        text = text_page.text
        assert "Your basket is empty." in text

    def bascet_text_not_true(self):
        text_page = self.browser.find_element(*BascetPageLocators.BASCET_TEXT)
        text = text_page.text
        assert "Your basket is empty." not in text