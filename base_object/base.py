from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import log_method
import logging as log

class BaseObject:
    log = log_method(logLevel=log.INFO)
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        """
        Check element is visible
        :param locator: visible element
        :return: visible element
        """
        self.log.info(f'Element {locator}  is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        self.log.info(f'Element {locator}  is clickable')
        return self.wait.until(ec.element_to_be_clickable(locator))

    def to_click(self, locator):
        self.log.info(f'Element {locator}   clicked')
        self.is_visible(locator).click()

    def to_send_keys(self, locator, keys):
        self.log.info(f'For {locator}  sended: {keys}')
        self.is_visible(locator).send_keys(keys)

    def get_text(self, locator):
        self.log.info(f'From {locator}  taken text')

        return self.is_visible(locator).text

    def get_itemname(self, locator):
        item_name = self.get_text(locator)
        return item_name

