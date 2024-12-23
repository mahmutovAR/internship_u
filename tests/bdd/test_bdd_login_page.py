import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers

from pages import LoginPage


scenarios('./features/login_page.feature')


@pytest.fixture
def login(browser: fixture):
    return LoginPage(browser)


@given('Login page')
def open_page(login: fixture):
    login.open_login_page()


@then('"Username" "Password" "Username *" fields are present, labels are correct')
def assert_fields_and_labels(login: fixture):
    login.check_username_field_label()
    login.check_password_field_label()
    login.check_username_desc_field_label()


@when('Click all fields without entering data')
def click_fields(login: fixture):
    login.click_username_field()
    login.click_password_field()
    login.click_username_desc_field()
    login.click_somewhere()


@then('Error messages are displayed and "Login" button is not clickable')
def check_fields_errors_and_login_button(login: fixture):
    login.check_username_error()
    login.check_password_error()
    login.check_username_desc_error()
    login.check_login_button_is_not_enabled()


@when(parsers.parse('Log in with valid data: "{username}" "{password}" "{username_desc}"'))
def log_in_with_valid_data(login: fixture, username: str, password: str, username_desc: str):
    login.fill_username(username)
    login.fill_password(password)
    login.fill_username_desc(username_desc)
    login.click_login_button()


@then('Authentication is successful')
def valid_data_check_auth(login: fixture):
    login.assert_auth_success()


@when(parsers.parse('Log in with invalid data: {username} {password} {username_desc}'))
def log_in_with_invalid_data(login: fixture, username: str, password: str, username_desc: str):
    login.fill_username(username)
    login.fill_password(password)
    login.fill_username_desc(username_desc)
    login.click_login_button()


@then('Error message is displayed')
def invalid_data_check_auth(login: fixture):
    login.assert_auth_error()


@when(parsers.parse('Log in with incorrect data: {username} {password} {username_desc}'))
def enter_invalid_data(login: fixture, username: str, password: str, username_desc: str):
    login.fill_username(username)
    login.fill_password(password)
    login.fill_username_desc(username_desc)
    login.click_somewhere()


@then(parsers.parse('Corresponding error message is displayed: {username_error} {password_error} {username_desc_error}'))
def check_fields_error(login: fixture, username_error: str, password_error: str, username_desc_error: str):
    if username_error.lower() == 'true':
        username_error = True
    else:
        username_error = False
    if password_error.lower() == 'true':
        password_error = True
    else:
        password_error = False
    if username_desc_error.lower() == 'true':
        username_desc_error = True
    else:
        username_desc_error = False
    login.assert_field_error(username_error, password_error, username_desc_error)


@when('log out')
def log_out(login: fixture):
    login.click_logout_button()


@then('Login page is displayed')
def check_login_page(login: fixture):
    login.check_username_field_label()
    login.check_password_field_label()
    login.check_username_desc_field_label_after_logout()
