import allure
import pytest
from allure import severity_level
from pytest import fixture

from data import BasicAuthData
from pages import BasicAuthPage


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Alert input")
@allure.testcase("Задача U13")
@allure.story("""Нажать "Display Image", ввести логин и пароль""")
@allure.title("Ввод логина и пароля в всплывающем окно")
@allure.description(
    """
    Цель: Проверить ввод логина и пароля в всплывающем окно

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу
        2. Нажать "Display Image"
        3. Ввести логин и пароль
        4. Проверить, что авторизация прошла успешно

    Ожидаемый результат:
        - После ввода в всплывающем окне логина и пароля, авторизация прошла успешно""")
@pytest.mark.parametrize('login, password', [(BasicAuthData.login, BasicAuthData.password)])
def test_alert_log_in(browser: fixture, login: str, password: str):
    alerts_page = BasicAuthPage(browser)
    alerts_page.open_page()
    alerts_page.click_display_image()
    alerts_page.enter_login_and_password(login, password)
    alerts_page.assert_authorization()
