import pytest
import allure

@allure.description('Test succ login using correct creds')
@allure.label('owner', 'alex')
@allure.title('Successful login')
@allure.suite('authorization')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.ui
def test_successful_login(index_page):
    with allure.step('fill login field'):
        index_page.fill_login_field()
    with allure.step('fill password field'):
        index_page.fill_password_field()
    with allure.step('click login button'):
        index_page.click_login_button()
    with allure.step('assert title in main page'):
        index_page.assert_title()


@pytest.mark.ui
def test_unsuccessful_login(index_page):
    index_page.fill_login_field_invalid_credentials()
    index_page.fill_password_field()
    index_page.click_login_button()
    index_page.assert_error_message()



