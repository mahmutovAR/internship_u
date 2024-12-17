import pytest
from pytest import fixture

from pages import RegistrationPage, LoginPage, Menu
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('./features/failure_screenshot.feature')


@pytest.fixture
def reg_form(browser: fixture):
    return RegistrationPage(browser)


@given('Registration Page Form')
def reg_form_open_page(reg_form: fixture):
    reg_form.open_form_page()


@when('Click "SUBMIT"')
def reg_form_click_submit(reg_form: fixture):
    reg_form.submit_data()


@then('No error messages')
def reg_form_check_log_in(reg_form: fixture):
    reg_form.no_error_found()


@pytest.fixture
def login_form(browser: fixture):
    return LoginPage(browser)


@given('Login Page Form')
def login_form_open_page(login_form: fixture):
    login_form.open_login_page()


@when(parsers.parse('Log in with invalid username "{username}" password "{password}" and username * "{username_desc}"'))
def login_form_enter_data(login_form: fixture, username: str, password: str, username_desc: str):
    login_form.fill_username(username)
    login_form.fill_password(password)
    login_form.fill_username_desc(username_desc)
    login_form.click_login_button()


@then('Authentication is successful')
def login_form_check_auth(login_form: fixture):
    login_form.assert_auth_success()


@pytest.fixture
def redirection(browser: fixture):
    return Menu(browser)


@given('Homepage')
def redirection_open_page(redirection: fixture):
    redirection.open_homepage()


@when('Hover over menu')
def redirection_hover_over_all_courses(redirection: fixture):
    redirection.hover_over_all_courses()


@then('Successful redirection')
def assert_redirection(redirection: fixture):
    redirection.assert_redirection_to_appium_python()
    redirection.check_page_title("Appium Python Online Training in USA, India | Way2Automation")
    redirection.appium_python_elements_are_active()
