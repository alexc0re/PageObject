from base_object.base import BaseObject
from base_object.locators import Locators
from support.asserton import Assertion
import os
import json
from pathlib import Path


FULL_PATH = os.path.dirname(os.path.abspath(__file__))
PATH = Path(FULL_PATH).parent
#PATH = os.path.dirname(FULL_PATH)
cred_path = str(PATH)+'/support/passwords.json'
creds_file = open(cred_path, 'rb')
creds = json.load(creds_file)

USERNAME = creds['correct_username']
PASSWORD = creds['correct_password']


class IndexPage(BaseObject, Assertion):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def fill_login_field(self):
        global USERNAME
        self.to_send_keys(Locators.USERNAME, USERNAME)

    def fill_login_field_invalid_credentials(self):
        self.to_send_keys(Locators.USERNAME, 'user')

    def fill_password_field(self):
        global PASSWORD
        self.to_send_keys(Locators.PASSWORD, PASSWORD)

    def click_login_button(self):
        self.to_click(Locators.LOGIN_BUTTON)

    def assert_title(self):
        self.assertion_equal('PRODUCTS', self.get_text(Locators.TITLE))

    def assert_error_message(self):
        self.assertion_equal('Epic sadface: Username and password do not match any user in this service', self.get_text(Locators.LOGIN_ERROR_MESSAGE))

