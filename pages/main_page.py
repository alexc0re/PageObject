import pytest

from base_object.base import BaseObject
from base_object.locators import Locators


class MainPage(BaseObject):
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
        self.assertion('PRODUCTS', self.get_text(Locators.TITLE))

    def assert_backpack(self):
        self.assertion('Sauce Labs Backpack', self.get_text(Locators.BACKPACK_ITEM))

    def click_on_product(self, locator):
        self.to_click(locator)
