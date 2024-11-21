import pytest
from pytest import fixture

from pages import LoginPage


def test_login_page(browser: fixture):
    """Checks that form elements are present.
    4.1 Проверка полей ввода
    - Поля "Username" и "Password" отображаются корректно."""
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.check_fields()


def test_empty_form(browser: fixture):
    """Checks empty form submitting.
    4.1 Проверка полей ввода
    - Поля валидируются при попытке отправить пустую форму:
        - Ошибки валидации отображаются для незаполненных полей."""
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.check_empty_form()


@pytest.mark.parametrize('username, password, username_desc', [('angular', 'password', 'angular b')])
def test_log_in(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with valid data.
    4.2 Проверка успешной авторизации
    - Ввести валидные username и password, нажать на кнопку Login.
    - Ожидаемый результат: отображается сообщение об успешной авторизации ("You're logged in!!")."""
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.log_in_valid(username, password, username_desc)


@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'angular c')])
def test_log_in_invalid(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with invalid data.
    4.3 Проверка авторизации с невалидными данными
    - Ввести невалидный username или password и нажать Login.
    - Ожидаемый результат: отображается сообщение об ошибке ("Username or password is incorrect")."""
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.log_in_invalid(username, password, username_desc)


@pytest.mark.parametrize('username, password, username_desc', [('angular', 'password', 'angular b')])
def test_log_out(browser: fixture, username: str, password: str, username_desc: str):
    """Checks for login with valid data and logout.
    4.4 Проверка успешного разлогирования
    - Нажать на кнопку "Logout".
    - Ожидаемый результат: отображаются поля для входа."""
    login_page = LoginPage(browser)
    login_page.go_to_login_page()
    login_page.log_in_valid(username, password, username_desc)
    login_page.log_out()


@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'angular c'),
                                                               ('invalid username', 'invalid password', 'angular c'),
                                                               ('invalid username', 'invalid password', 'angular c'),
                                                               ('invalid username', 'invalid password', 'angular c'),
                                                               ('invalid username', 'invalid password', 'angular c'),])
def test_log_in_invalid_extended(browser: fixture, username: str, password: str, username_desc: str):
    pass
