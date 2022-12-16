def test_some(main_page):
    main_page.fill_login_field()
    main_page.fill_password_field()
    main_page.click_login_button()
    main_page.assert_backpack()