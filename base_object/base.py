from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BaseObject:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def to_click(self, locator):
        self.is_visible(locator).click()

    def to_send_keys(self, locator, keys):
        self.is_visible(locator).send_keys(keys)

    def get_text(self, locator):
        return self.is_visible(locator).text

    def get_itemname(self, locator):
        item_name = self.get_text(locator)
        return item_name

    @staticmethod
    def assertion(expected, actual):
        assert expected == actual, f'Failed, expected: {expected}, but got: {actual}'
