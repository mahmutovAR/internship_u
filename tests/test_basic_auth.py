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
@allure.story("""Открыть страницу, пройти базовую аутентификацию""")
@allure.title("Базовая аутентификация")
@allure.description(
    """
    Цель: Проверить базовую аутентификацию

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу со встроенным username и password для базовой аутентификации
        2. Проверить, что "Authenticated Image" не отображается
        2. Нажать "Display Image"
        3. Проверить, что "Authenticated Image" не отображается

    Ожидаемый результат:
        - Базовая аутентификация прошла успешно""")
@pytest.mark.parametrize('username, password', [(BasicAuthData.username, BasicAuthData.password)])
def test_basic_auth(browser: fixture, username: str, password: str):
    basic_auth = BasicAuthPage(browser)
    basic_auth.open_page(username, password)
    with allure.step('Проверить, что "Authenticated Image" не отображается'):
        assert not basic_auth.auth_image_is_visible(), 'Authenticated Image expected not to be visible'
    basic_auth.click_display_image()
    with allure.step('Проверить, что "Authenticated Image" отображается'):
        assert basic_auth.auth_image_is_visible(), 'Authenticated Image expected to be visible'
