import time

import pytest

from base_object.base import BaseObject
from base_object.locators import Locators
from support.asserton import Assertion


class MainPage(BaseObject, Assertion):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_login_field(self):
        self.to_send_keys(Locators.USERNAME, 'standard_user')

    def fill_password_field(self):
        self.to_send_keys(Locators.PASSWORD, 'secret_sauce')

    def click_login_button(self):
        self.to_click(Locators.LOGIN_BUTTON)

    def assert_title(self):
        self.assertion_equal('PRODUCTS', self.get_text(Locators.TITLE))

    def assert_backpack(self):
        self.assertion_equal('Sauce Labs Backpack', self.get_text(Locators.BACKPACK_ITEM))

    def click_to_basket_btn(self):
        self.to_click(Locators.ADD_TO_BASKET_BUTTON)

    def go_to_basket_from_product_page(self):
        self.to_click(Locators.CART_BUTTON)

    def checkout_button_is_displayed(self):
        self.is_visible(Locators.CHECKOUT_BUTTON)




