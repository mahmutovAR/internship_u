import allure
import pytest
from allure import severity_level
from pytest import fixture

from pages import RegistrationPage, LoginPage, Menu


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("Скриншот упавшего теста")
@allure.testcase("Задачи U1, U2, U4")
@allure.story("При падении теста делается скриншот")
@allure.title("Авторизация на странице Registration Page")
@allure.description(
    """
    Цель: Проверить обработку упавших тестов

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Нажать на кнопку "SUBMIT"
        3. Проверить отсутствие сообщений об ошибках

    Ожидаемый результат:
        - Нет сообщений о некорректном вводе данных""")
def test_fill_out_form(browser: fixture):
    login_page = RegistrationPage(browser)
    login_page.open_form_page()
    login_page.submit_data()
    login_page.no_error_found()


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("Скриншот упавшего теста")
@allure.testcase("Задачи U1, U2, U4")
@allure.story("При падении теста делается скриншот")
@allure.title("Авторизация на странице Login Page")
@allure.description(
    """
    Цель: Проверить обработку упавших тестов

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
@pytest.mark.parametrize('username, password, username_desc', [('invalid username', 'invalid password', 'username-C')])
def test_log_in(browser: fixture, username: str, password: str, username_desc: str):
    login_page = LoginPage(browser)
    login_page.open_login_page()
    login_page.fill_username(username)
    login_page.fill_password(password)
    login_page.fill_username_desc(username_desc)
    login_page.click_login_button()
    login_page.assert_auth_success()


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("Скриншот упавшего теста")
@allure.testcase("Задачи U1, U2, U4")
@allure.story("При падении теста делается скриншот")
@allure.title("Переход по меню на другие страницы")
@allure.description(
    """
    Цель: Проверка перехода по меню на другие страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Навести курсор на вкладку меню "All Courses"
        3. Кликнуть пункт "Appium"
        4. Кликнуть пункт "Appium with Python"
        5. Проверить переход на страницу
        6. Проверить значение "TITLE"
        7. Проверить корректность отображения элементов страницы

    Ожидаемый результат:
        - Происходит переход на страницу
        - Значение "TITLE" соответствует странице
        - Элементы, уникальные для этой страницы, активны""")
def test_redirect_to_appium_python(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_all_courses()
    menu.assert_redirection_to_appium_python()
    menu.check_page_title("Appium Python Online Training in USA, India | Way2Automation")
    menu.appium_python_elements_are_active()
