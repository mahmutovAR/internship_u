import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import AuthCookiesData
from pages import AuthCookiesPage


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Авторизация")
@allure.testcase("Задачи U5")
@allure.story("Успешная авторизация и сохранение cookies в файл")
@allure.title("Авторизация на странице SQL exercises")
@allure.description(
    """
    Цель: Авторизация и сохранение cookies в файл

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Ввести данные в поле "Login"
        3. Ввести данные в поле "Password"
        4. Кликнуть кнопку "Enter"
        
        . Проверить, что отображается сообщение об успешной авторизации
        
        . Сохранить cookies в файл
        . Проверить, что файл с cookies создан
        

    Ожидаемый результат:
        - Авторизация прошла успешно
        - cookies файл создан""")
@pytest.mark.parametrize('username, password',
                         [(AuthCookiesData.login, AuthCookiesData.password)])
@pytest.mark.dependency()
def Rtest_log_in_and_save_cookies(browser: fixture, username: str, password: str):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_login_page()
    auth_page.fill_login(username)
    auth_page.fill_password(password)
    auth_page.click_enter_button()

    auth_page.get_and_save_cookies()
    auth_page.assert_cookies_file_exists()


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
        2. Загрузить cookies из файла
        5. Кликнуть кнопку "Enter"
        
        . Проверить, что отображается сообщение об успешной авторизации
        . Кликнуть кнопку "Logout"

    Ожидаемый результат:
        - Авторизация прошла успешно
        - Отображается сообщение об успешной авторизации""")
@pytest.mark.dependency(depends=["test_log_in_and_save_cookies"])
def Rtest_log_in_with_cookies(browser: fixture):
    auth_page = AuthCookiesPage(browser)
    auth_page.open_login_page()
    auth_page.load_cookies()

    auth_page.refresh_page()
