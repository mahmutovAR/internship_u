from pytest import fixture
import pytest
from pages import LoginPage


def test_login_page(browser: fixture):
    """Checks that the lo page loads and that form elements are present."""
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.page_loaded()
    login_page.check_fields()


def test_empty_form(browser: fixture):
    """Checks empty form submitting."""
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.check_empty_form()


@pytest.mark.parametrize('username, password, username_desc', [('angular', 'password', 'angular b')])
def test_log_in(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with valid data."""
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.log_in_valid(username, password, username_desc)


@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'angular c')])
def test_log_in_invalid(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with invalid data."""
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.log_in_invalid(username, password, username_desc)


@pytest.mark.parametrize('username, password, username_desc', [('angular', 'password', 'angular b')])
def test_log_out(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with valid data and logout."""
    login_page = LoginPage(browser)
    login_page.go_to_login()
    login_page.log_in_valid(username, password, username_desc)
    login_page.log_out()
