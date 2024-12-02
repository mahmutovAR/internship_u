import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import LoginData
from pages import LoginPage


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Страница загружается успешно, основные элементы отображаются корректно")
@allure.title("Авторизация на странице Login Page")
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
        5. Проверить описание поля "Username"
        6. Проверить описание поля "Password"
        7. Проверить описание поля "Username *"

    Ожидаемый результат:
        - Поля отображаются
        - Описания соответствуют полям""")
def test_login_page(browser: fixture):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.check_username_field_label()
    login_page.check_password_field_label()
    login_page.check_username_desc_field_label()


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Отправка пустой формы невозможна")
@allure.title("Авторизация на странице Login Page")
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
        6. Проверить сообщение с ошибкой незаполненного поля "Username"
        7. Проверить сообщение с ошибкой незаполненного поля "Password"
        8. Проверить цвет описания поля "Username *"
        9. Проверить, что кнопка "Login" не активна

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
    login_page.check_username_error()
    login_page.check_password_error()
    login_page.check_username_desc_error()
    login_page.check_login_button_is_not_enabled()


@allure.severity(severity_level.CRITICAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Авторизация с корректными данными проходит успешно")
@allure.title("Авторизация на странице Login Page")
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
        6. Проверить, что отображается сообщение об успешной авторизации

    Ожидаемый результат:
        - Авторизация прошла успешно
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
    login_page.assert_auth_success()


@allure.severity(severity_level.CRITICAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Авторизация с некорректными данными не проходит")
@allure.title("Авторизация на странице Login Page")
@allure.description(
    """
    Цель: Проверить авторизацию с некорректными данными

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Ввести данные в поле "Username"
        3. Ввести данные в поле "Password"
        4. Ввести данные в поле "Username *"
        5. Кликнуть кнопку "Login"
        6. Проверить, что отображается сообщение о ошибке авторизации

    Ожидаемый результат:
        - Отображается сообщение об ошибке""")
@pytest.mark.parametrize('username, password, username_desc',
                         [('invalid username', 'invalid password', 'username-C', ),
                          (LoginData.username, 'invalid password', f'{LoginData.username}-AB'),
                          ('invalid username', LoginData.password, f'{LoginData.username}-AB')])
def test_log_in_invalid(browser: fixture, username: str, password: str, username_desc: str):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_login_button()
    login_page.assert_auth_error()


@allure.severity(severity_level.CRITICAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Авторизация с некорректными данными с проверкой ошибок")
@allure.title("Авторизация на странице Login Page")
@allure.description(
    """
    Цель: Проверить авторизацию с некорректными данными

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Ввести данные в поле "Username"
        3. Ввести данные в поле "Password"
        4. Ввести данные в поле "Username *"
        5. Кликнуть в пустую часть страницы
        6. Проверить, что отображаются сообщения о некорректном вводе

    Ожидаемый результат:
        - Отображаются соответствующие сообщения об ошибке
        - Кнопка "Login" не активна""")
@pytest.mark.parametrize('username, password, username_desc, username_error, password_error, username_desc_error',
                         [('ab', 'abcdefg', 'abcdefg', True, False, False),
                          ('abcdefg', 'ab', 'abcdefg', False, True, False),
                          ('abcdefg', 'abcdefg', 'ab', False, False, True),
                          ('abcdefg', 'ab', 'ab', False, True, True),
                          ('ab', 'abcdefg', 'ab', True, False, True),
                          ('ab', 'ab', 'abcdefg', True, True, False),
                          ('ab', 'ab', 'ab', True, True, True)])
def test_log_in_invalid_extended(browser: fixture, username: str, password: str, username_desc: str,
                                 username_error: bool, password_error: bool, username_desc_error: bool):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_somewhere()
    login_page.assert_field_error(username_error, password_error, username_desc_error)


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U1, U2")
@allure.story("Авторизация с корректными данными и успешное разлогирование")
@allure.title("Авторизация на странице Login Page")
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
        - Отображаются поля для входа""")
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
    login_page.check_username_field_label()
    login_page.check_password_field_label()
    login_page.check_username_desc_field_label_after_logout()
