import pytest
from pytest import fixture

from pages import RegistrationPage
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('./features/js_executor.feature')


@pytest.fixture
def registration(browser: fixture):
    return RegistrationPage(browser)


@given('Form page')
def registration_open_page(registration: fixture):
    registration.open_form_page()


@given('click "First Name" field')
def registration_click_filed(registration: fixture):
    registration.click_first_name_field()
    registration.click_first_name_field()
    registration.assert_focus_on_element()


@when('Remove focus from input field by using JavaScriptExecutor')
def registration_remove_focus(registration: fixture):
    registration.blur_first_name_field()


@then('Focus removed from input field')
def registration_check_focus(registration: fixture):
    registration.assert_element_not_active()


@given('Form page')
def registration_scroll_open_page(registration: fixture):
    registration.open_form_page()


@then('Use JavaScriptExecutor to assert page scroll')
def registration_assert_scroll(registration: fixture):
    registration.assert_page_scroll()
