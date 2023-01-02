import pytest
from base_object.locators import Locators


@pytest.mark.ui
@pytest.mark.smoke
def test_main_page_opened(main_page):
    main_page.fill_login_field()
    main_page.fill_password_field()
    main_page.click_login_button()
    main_page.assert_backpack()


@pytest.mark.smoke
@pytest.mark.parametrize('locator', (Locators.USERNAME, Locators.PASSWORD))
def test_user_can_buy_some_goods(main_page, locator):
    test_main_page_opened(main_page)
    main_page.click_on_product(locator)

