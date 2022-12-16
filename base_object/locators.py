from selenium.webdriver.common.by import By


class Locators:
    USERNAME = (By.CSS_SELECTOR, '#user-name')
    PASSWORD = (By.CSS_SELECTOR, '#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '#login-button')
    TITLE = (By.CSS_SELECTOR, '.title')
    LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"')

    BACKPACK_ITEM = (By.CSS_SELECTOR, '#item_4_title_link .inventory_item_name')
