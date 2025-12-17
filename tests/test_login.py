from pages.login_page import LoginPage

def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)

    login.open_url()
    login.login("tomsmith", "SuperSecretPassword!")

    success_text = login.get_success_message()
    assert "You logged into a secure area!" in success_text
