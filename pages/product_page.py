import time
from .locators import ProductBascetLocators, ProductPageLocators
from .base_page import BasePage


class ProductBascet(BasePage):
    def text_product(self):
        prod = self.browser.find_element(*ProductBascetLocators.TEXT_PRODUCT)
        prod_text = prod.text
        return prod_text
    
    def price_product(self):
        prod_price = self.browser.find_element(*ProductBascetLocators.PRICE_PRODUCT)
        price_prod = prod_price.text
        return price_prod

    def guest_can_add_product_to_basket(self):
        button = self.browser.find_element(*ProductBascetLocators.ADD_BASCET)
        button.click()

    def text_product_bascet(self):
        bascet_prod = self.browser.find_element(*ProductBascetLocators.BASCET_TEXT_PRODUCT)
        bascet_text_prod = bascet_prod.text
        return bascet_text_prod

    def price_product_bascet(self):
        bascet_price = self.browser.find_element(*ProductBascetLocators.BASCET_PRICE_PRODUCT)
        bascet_price_text = bascet_price.text
        return bascet_price_text

    def text_and_price_product_comparison_bascet(self):
        assert self.text_product_bascet() in self.text_product()
        assert self.price_product_bascet() in self.price_product()
        time.sleep(10)

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "message is present, is not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "message two is present, NOT"



        




