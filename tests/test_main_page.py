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
@pytest.mark.parametrize('locator', (Locators.BACKPACK_ITEM, Locators.BIKE_LIGHT_ITEM, Locators.BOLT_TSHIRT_ITEM))
def test_user_can_add_some_goods_to_basket(main_page, locator):
    test_main_page_opened(main_page)
    main_page.get_itemname(locator)
    main_page.to_click(locator)
    main_page.click_to_basket_btn()
    main_page.go_to_basket_from_product_page()
    main_page.checkout_button_is_displayed()


