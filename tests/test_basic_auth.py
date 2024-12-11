import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import BasicAuthData
from pages import BasicAuthPage


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Basic Auth")
@allure.testcase("Задача U13")
@allure.story("""Открыть страницу, пройти базовую авторизацию""")
@allure.title("Базовая авторизация")
@allure.description(
    """
    Цель: Проверить базовую авторизацию

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу
        2. Нажать "Display Image"
        3. Авторизироваться с корректными "username" и "password"
        4. Проверить, что авторизация прошла успешно

    Ожидаемый результат:
        - Базовая авторизация прошла успешно""")
@pytest.mark.parametrize('username, password', [(BasicAuthData.username, BasicAuthData.password)])
def test_basic_auth(browser: fixture, username: str, password: str):
    basic_auth = BasicAuthPage(browser)
    basic_auth.open_page()
    basic_auth.click_display_image()
    status_code = basic_auth.log_in(username, password)
    with allure.step('Проверить, что авторизация прошла успешно'):
        assert status_code == 200, f'Expected status code 200, but got "{status_code}"'
