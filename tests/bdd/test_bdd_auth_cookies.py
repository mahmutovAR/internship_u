import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers

from helpers import cookie_helper
from pages import AuthCookiesPage, AltAuthCookiesPage


scenarios('./features/auth_cookies.feature')


@pytest.fixture
def auth(browser: fixture):
    return AuthCookiesPage(browser)


@given('"Form 1" page')
def auth_open_page(auth: fixture):
    auth.open_auth_page()
    auth.check_auth_form()


@when(parsers.parse('Log in "Form 1" with valid data: {username} {password}'))
def auth_log_in(auth: fixture, username: str, password: str):
    auth.fill_username(username)
    auth.fill_password(password)
    auth.click_login()


@then('Auth "Form 1" is successful, save cookies into file')
def auth_check_log_in(auth: fixture):
    auth.check_guest_authentication()
    cookies = auth.get_cookies_data()
    cookie_helper.save_cookies_to_file(cookies)
    auth.click_logout_button()
    auth.check_auth_form()
    assert cookie_helper.file_exists(), 'Cookies file expected to be created'


@when('Load "Form 1" cookies from file')
def auth_load_cookies(auth: fixture):
    auth.delete_cookies()
    auth.load_cookies_data(cookie_helper.load_cookies_from_file())


@then('Auth "Form 1" is successful')
def auth_with_cookies_check_log_in(auth: fixture, delete_cookies_file: fixture):
    auth.open_auth_page()
    auth.check_guest_authentication()
    auth.click_logout_button()
    auth.check_auth_form()


@pytest.fixture
def auth_alt(browser: fixture):
    return AltAuthCookiesPage(browser)


@given('"Form 2" page')
def auth_alt_open_page(auth_alt: fixture):
    auth_alt.open_auth_page()
    auth_alt.check_auth_form()


@when(parsers.parse('Log in "Form 2" with valid data: {username} {password}'))
def auth_alt_log_in(auth_alt: fixture, username: str, password: str):
    auth_alt.fill_username(username)
    auth_alt.fill_password(password)
    auth_alt.click_login()


@then('Auth "Form 2" is successful, save cookies into file')
def auth_alt_check_log_in(auth_alt: fixture):
    assert auth_alt.check_authorization(), 'Expected authorization to be successful'
    cookies = auth_alt.get_cookies_data()
    cookie_helper.save_cookies_to_file(cookies)
    auth_alt.click_logout()
    auth_alt.check_auth_form()
    assert cookie_helper.file_exists(), 'Cookies file expected to be created'


@when('Load cookies "Form 2" from file')
def auth_alt_load_cookies(auth_alt: fixture):
    assert not auth_alt.check_authorization(), 'Expected no authorization'
    auth_alt.delete_cookies()
    auth_alt.load_cookies_data(cookie_helper.load_cookies_from_file())
    auth_alt.open_logged_page()
    assert auth_alt.check_authorization(), 'Expected authorization to be successful'
    auth_alt.click_logout()
    auth_alt.check_auth_form()


@then('Auth "Form 2" is successful')
def auth_alt_with_cookies_check_log_in(auth_alt: fixture, delete_cookies_file: fixture):
    auth_alt.open_logged_page()
    assert auth_alt.check_authorization(), 'Expected authorization to be successful'
    auth_alt.click_logout()
    auth_alt.check_auth_form()
    auth_alt.open_logged_page()
    assert auth_alt.check_authorization(), 'Expected authorization to be successful'
    auth_alt.click_logout()
    auth_alt.check_auth_form()
