import allure
import pytest
from allure import severity_level
from pytest import fixture

from pages import RegistrationPage, LoginPage, Menu


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Test failure screenshot")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Скриншот упавшего теста")
@allure.description(
    """
    Цель: Проверить обработку упавших тестов

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой "Registration Form"
        2. Нажать на кнопку "SUBMIT"

    Ожидаемый результат:
        - Вывод сообщений под пустыми полями
        - Сделан скриншот упавшего теста""")
def test_fill_out_form(browser: fixture):
    login_page = RegistrationPage(browser)
    login_page.open_form_page()
    login_page.submit_data()
    login_page.no_error_found()


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Test failure screenshot")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Скриншот упавшего теста")
@allure.description(
    """
    Цель: Проверить обработку упавших тестов

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой "Login Page"
        2. Ввести некорректные данные в поле "Username"
        3. Ввести некорректные данные в поле "Password"
        4. Ввести данные в поле "Username *"
        5. Кликнуть кнопку "Login"

    Ожидаемый результат:
        - Авторизация не прошла
        - Сделан скриншот упавшего теста""")
@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'username-C')])
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


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Test failure screenshot")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Скриншот упавшего теста")
@allure.description(
    """
    Цель: Проверить обработку упавших тестов

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Навести курсор на вкладку меню "All Courses"

    Ожидаемый результат:
        - Переход на другую страницу не произошел
        - Сделан скриншот упавшего теста""")
def test_redirect_to_appium_python(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_all_courses()
    menu.assert_redirection_to_appium_python()
    menu.appium_python_elements_are_active()

