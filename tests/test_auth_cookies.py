import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import AuthCookiesData, AltAuthCookiesData
from pages import AuthCookiesPage, AltAuthCookiesPage
from helpers import cookie_helper


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задача U5")
@allure.story("Успешная авторизация и сохранение cookies в файл")
@allure.title("Авторизация на странице SQL exercises")
@allure.description(
    """
    Цель: Авторизация и сохранение cookies в файл

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Проверить, что доступны поля авторизации
        3. Ввести данные в поле "Username"
        4. Ввести данные в поле "Password"
        5. Кликнуть кнопку "Enter"
        6. Проверить, что авторизация прошла под именем "guest"
        7. Сохранить cookies в файл
        8. Кликнуть кнопку "logout"
        9. Проверить, что доступны поля авторизации
        10. Проверить, что файл с cookies создан

    Ожидаемый результат:
        - Авторизация прошла успешно
        - Файл с cookies создан""")
@pytest.mark.dependency()
def test_log_in_and_save_cookies(browser: fixture):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_auth_page()
    auth_page.check_auth_form()
    auth_page.fill_username(AuthCookiesData.username)
    auth_page.fill_password(AuthCookiesData.password)
    auth_page.click_login()
    auth_page.check_guest_authentication()
    with allure.step('Сохранить cookies в файл'):
        cookies = auth_page.get_cookies_data()
        cookie_helper.save_cookies_to_file(cookies)
    auth_page.click_logout_button()
    auth_page.check_auth_form()
    with allure.step('Проверить, что файл с cookies создан'):
        assert cookie_helper.file_exists(), 'Cookies file expected to be created'


@allure.severity(severity_level.CRITICAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задача U5")
@allure.story("Успешная авторизация с загрузкой из файла cookies")
@allure.title("Авторизация на странице SQL exercises")
@allure.description(
    """
    Цель: Проверить авторизацию используя загрузку cookies

    Предусловие:
        - Открыть браузер

    Шаги:        
        1. Открыть страницу с формой
        2. Проверить, что доступны поля авторизации
        3. Удалить cookies
        4. Загрузить cookies из файла
        5. Открыть страницу успешной авторизации
        6. Проверить, что авторизация прошла под именем "guest"
        6. Кликнуть кнопку "logout"
        7. Проверить, что доступны поля авторизации
        
    Постусловие:
        - Удалить файл с cookies

    Ожидаемый результат:
        - Авторизация прошла успешно""")
@pytest.mark.dependency(depends=["test_log_in_and_save_cookies"])
def test_load_cookies(browser: fixture, delete_cookies_file: fixture):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_auth_page()
    auth_page.check_auth_form()
    auth_page.delete_cookies()
    with allure.step('Загрузить cookies из файла'):
        auth_page.load_cookies_data(cookie_helper.load_cookies_from_file())
    auth_page.open_auth_page()
    auth_page.check_guest_authentication()
    auth_page.click_logout_button()
    auth_page.check_auth_form()


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задача U5")
@allure.story("Успешная авторизация и сохранение cookies в файл")
@allure.title("Авторизация на странице the-internet.herokuapp.com")
@allure.description(
    """
    Цель: Авторизация и сохранение cookies в файл

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Проверить, что доступны поля авторизации
        3. Ввести данные в поле "Username"
        4. Ввести данные в поле "Password"
        5. Кликнуть кнопку "Login"
        6. Проверить, что авторизация прошла успешно
        7. Сохранить cookies в файл
        8. Кликнуть кнопку "Logout"
        9. Проверить, что доступны поля авторизации
        10. Проверить, что файл с cookies создан

    Ожидаемый результат:
        - Авторизация прошла успешно
        - Файл с cookies создан""")
@pytest.mark.dependency()
def test_alt_log_in_and_save_cookies(browser: fixture):
    auth_page = AltAuthCookiesPage(browser)
    auth_page.open_auth_page()
    auth_page.check_auth_form()
    auth_page.fill_username(AltAuthCookiesData.username)
    auth_page.fill_password(AltAuthCookiesData.password)
    auth_page.click_login()
    with allure.step('Проверить, что авторизация прошла успешно'):
        assert auth_page.check_authorization(), 'Expected authorization to be successful'
    with allure.step('Сохранить cookies в файл'):
        cookies = auth_page.get_cookies_data()
        cookie_helper.save_cookies_to_file(cookies)
    auth_page.click_logout()
    auth_page.check_auth_form()
    with allure.step('Проверить, что файл с cookies создан'):
        assert cookie_helper.file_exists(), 'Cookies file expected to be created'


@allure.severity(severity_level.CRITICAL)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задача U5")
@allure.story("Успешная авторизация с загрузкой из файла cookies")
@allure.title("Авторизация на странице the-internet.herokuapp.com")
@allure.description(
    """
    Цель: Проверить авторизацию используя загрузку cookies

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу успешной авторизации
        2. Проверить, что вход не выполнен
        3. Удалить cookies
        4. Загрузить cookies из файла
        5. Открыть страницу успешной авторизации
        6. Проверить, что авторизация прошла успешно
        6. Кликнуть кнопку "Logout"
        7. Проверить, что доступны поля авторизации

    Постусловие:
        - Удалить файл с cookies

    Ожидаемый результат:
        - Авторизация прошла успешно""")
@pytest.mark.dependency(depends=["test_alt_log_in_and_save_cookies"])
def test_alt_load_cookies(browser: fixture, delete_cookies_file: fixture):
    auth_page = AltAuthCookiesPage(browser)
    auth_page.open_logged_page()
    with allure.step('Проверить, что вход не выполнен'):
        assert not auth_page.check_authorization(), 'Expected no authorization'
    auth_page.delete_cookies()
    with allure.step('Загрузить cookies из файла'):
        auth_page.load_cookies_data(cookie_helper.load_cookies_from_file())
    auth_page.open_logged_page()
    with allure.step('Проверить, что авторизация прошла успешно'):
        assert auth_page.check_authorization(), 'Expected authorization to be successful'
    auth_page.click_logout()
    auth_page.check_auth_form()
