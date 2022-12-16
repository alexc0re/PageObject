def test_successful_login(index_page):
    index_page.fill_login_field()
    index_page.fill_password_field()
    index_page.click_login_button()
    index_page.assert_title()


def test_unsuccessful_login(index_page):
    index_page.fill_login_field_invalid_credentials()
    index_page.fill_password_field()
    index_page.click_login_button()
    index_page.assert_error_message()