import pytest
from .pages.base_page import BasePage
from .pages.bascet_page import BascetPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BascetPage(browser, link)
    page.open()
    page.go_to_add_bascet_page()
    page.bascet_text_true()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/applied-cryptography_200/"
    page = BascetPage(browser, link)
    page.open()
    page.go_to_add_bascet_page()
    page.bascet_text_true()

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, link)
        page.open()
        page.go_to_login_page()


    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/"
        page = BasePage(browser, link)
        page.open()
        page.should_be_login_link()
