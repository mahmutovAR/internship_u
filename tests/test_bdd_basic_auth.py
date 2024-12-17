import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers

from pages import BasicAuthPage


scenarios('./features/basic_auth.feature')


@pytest.fixture
def basic_auth(browser: fixture):
    return BasicAuthPage(browser)


@given('Basic Auth page')
def open_page(basic_auth: fixture):
    basic_auth.open_page()


@when('Click "Display Image"')
def click_button(basic_auth: fixture):
    basic_auth.click_display_image()


@when(parsers.parse('Log in with valid username "{username}" and password "{password}"'))
def log_in_with_valid_data(basic_auth: fixture, username: str, password: str, data_storage: fixture):
    data_storage['status_code'] = basic_auth.log_in(username, password)


@then('Authentication is successful')
def check_log_in(data_storage: fixture):
    assert data_storage['status_code'] == 200, f'Expected status code 200, but got "{data_storage['status_code']}"'
