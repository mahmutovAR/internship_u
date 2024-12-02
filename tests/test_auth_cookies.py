import allure
import pytest
from allure import severity_level
from pytest import fixture

from pages import AuthCookiesPage
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
        3. Кликнуть кнопку "Enter without login"
        4. Проверить, что авторизация прошла под именем "guest"
        5. Сохранить cookies в файл
        6. Кликнуть кнопку "logout"
        7. Проверить, что доступны поля авторизации
        8. Проверить, что файл с cookies создан

    Ожидаемый результат:
        - Авторизация прошла успешно
        - файл с cookies создан""")
@pytest.mark.dependency()
def test_log_in_and_save_cookies(browser: fixture):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_auth_page()
    auth_page.check_auth_form()
    auth_page.click_enter_without_login_button()
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
        5. Обновить страницу
        6. Проверить, что авторизация прошла под именем "guest"
        6. Кликнуть кнопку "logout"
        7. Проверить, что доступны поля авторизации
        
    Постусловие:
        - Удалить файл с cookies

    Ожидаемый результат:
        - Авторизация прошла успешно""")
@pytest.mark.dependency(depends=["test_log_in_and_save_cookies"])
def test_log_in_with_cookies(browser: fixture, delete_cookies_file: fixture):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_auth_page()
    auth_page.check_auth_form()
    auth_page.delete_cookies()
    with allure.step('Загрузить cookies из файла'):
        auth_page.load_cookies_data(cookie_helper.load_cookies_from_file())
    auth_page.refresh_page()
    auth_page.check_guest_authentication()
    auth_page.click_logout_button()
    auth_page.check_auth_form()
    delete_cookies_file()
