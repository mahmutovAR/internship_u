import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import LoginData
from pages import LoginPage


@allure.severity(severity_level.BLOCKER)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Login Page")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка полей формы")
@allure.description(
    """
    Цель: Проверить поля ввода

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть страницу с формой
         2. Проверить наличие поля ввода "Username"
         3. Проверить наличие поля ввода "Password"
         4. Проверить наличие поля ввода "Username *"

    Ожидаемый результат:
        - Поля отображаются
        - Описания полей соответствуют им""")
def test_login_page(browser: fixture):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    username_label = login_page.find_username_field()
    password_label = login_page.find_password_field()
    username_desc_label = login_page.find_username_desc_field()
    assert username_label == 'Username', f'Expected label is "Username", but got {username_label}'
    assert password_label == 'Password', f'Expected label is "Password", but got {password_label}'
    assert username_desc_label == 'Username *', f'Expected label is "Username *", but got {username_desc_label}'


@allure.severity(severity_level.NORMAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Login Page")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка отправки пустой формы")
@allure.description(
    """
    Цель: Проверить отправку пустой формы

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть страницу с формой
         2. Кликнуть поле ввода "Username"
         3. Кликнуть поле ввода "Password"
         4. Кликнуть поле ввода "Username *"
         5. Кликнуть в пустую часть страницы

    Ожидаемый результат:
        - Ошибки валидации отображаются для незаполненных полей
        - Кнопка "Login" не активна""")
def test_empty_form(browser: fixture):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.click_username_field()
    login_page.click_password_field()
    login_page.click_username_desc_field()
    login_page.click_somewhere()
    expected_color = 'rgba(169, 68, 66, 1)'  # RGB value for #a94442
    field_color = login_page.check_username_desc_color()
    assert login_page.check_username_error(), 'Expected "Username" field error message'
    assert login_page.check_password_error(), 'Expected "Password" field error message'
    assert field_color == expected_color, f'Expected "Username *" field changes color to {expected_color}, but got {field_color}'
    assert not login_page.check_login_button_is_enabled(), f'Expected "Login" button is disabled'


@allure.severity(severity_level.CRITICAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Login Page")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка успешной авторизации")
@allure.description(
    """
    Цель: Проверить авторизацию

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть страницу с формой
         2. Ввести данные в поле "Username"
         3. Ввести данные в поле "Password"
         4. Ввести данные в поле "Username *"
         5. Кликнуть кнопку "Login"

    Ожидаемый результат:
        - Отображается сообщение об успешной авторизации""")
@pytest.mark.parametrize('username, password, username_desc',
                         [(LoginData.username, LoginData.password, f'{LoginData.username}-AB')])
def test_log_in(browser: fixture, username: str, password: str, username_desc: str):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_login_button()
    expected_message = "You're logged in!!"
    auth_message = login_page.assert_auth_success()
    assert auth_message == expected_message, f'Expected {expected_message} message, but got {auth_message}'


@allure.severity(severity_level.CRITICAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Login Page")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка авторизации с невалидными данными")
@allure.description(
    """
    Цель: Проверить авторизацию с невалидными данными

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть страницу с формой
         2. Ввести данные в поле "Username"
         3. Ввести данные в поле "Password"
         4. Ввести данные в поле "Username *"
         5. Кликнуть кнопку "Login"

    Ожидаемый результат:
        - отображается сообщение об ошибке""")
@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'username-C')])
def test_log_in_invalid(browser: fixture, username: str, password: str, username_desc: str):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_login_button()
    expected_message = "Username or password is incorrect"
    auth_message = login_page.assert_auth_error()
    assert auth_message == expected_message, f'Expected {expected_message} message, but got {auth_message}'


@allure.severity(severity_level.NORMAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Login Page")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка успешного разлогирования")
@allure.description(
    """
    Цель: Проверить разлогирование

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть страницу с формой
         2. Ввести данные в поле "Username"
         3. Ввести данные в поле "Password"
         4. Ввести данные в поле "Username *"
         5. Кликнуть кнопку "Login"
         6. Кликнуть кнопку "Logout"
         7. Проверить наличие поля ввода "Username"
         8. Проверить наличие поля ввода "Password"
         9. Проверить наличие поля ввода "Username *"

    Ожидаемый результат:
        - Отображается поля для входа""")
@pytest.mark.parametrize('username, password, username_desc',
                         [(LoginData.username, LoginData.password, f'{LoginData.username}-AB')])
def test_log_out(browser: fixture, username: str, password: str, username_desc: str):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_login_button()
    login_page.click_logout_button()
    username_label = login_page.find_username_field()
    password_label = login_page.find_password_field()
    username_desc_label = login_page.find_username_desc_field_after_logout()
    assert username_label == 'Username', f'Expected label is "Username", but got {username_label}'
    assert password_label == 'Password', f'Expected label is "Password", but got {password_label}'
    assert username_desc_label == 'Username *', f'Expected label is "Username *", but got {username_desc_label}'
