import allure
from allure import severity_level
from pytest import fixture

from pages import RegistrationPage


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("JavaScriptExecutor")
@allure.testcase("Задача U6")
@allure.story("Убрать фокус из поля ввода с помощью JavaScriptExecutor")
@allure.title("Загрузка страницы с Registration Form")
@allure.description(
    """
    Цель: Проверить работу JavaScriptExecutor

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Кликнуть поле ввода "First Name"
        3. Проверить, что фокус на поле ввода
        4. Убрать фокус из поля ввода с помощью JavaScriptExecutor
        5. Проверить, что поле ввода не в фокусе

    Ожидаемый результат:
        - После выполнения JavaScript поле ввода не в фокусе""")
def test_remove_focus(browser: fixture):
    registration_page = RegistrationPage(browser)
    registration_page.open_form_page()
    registration_page.click_first_name_field()
    registration_page.assert_focus_on_element()
    registration_page.blur_first_name_field()
    registration_page.assert_element_not_active()


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("JavaScriptExecutor")
@allure.testcase("Задача U6")
@allure.story("Проверка скролла на странице с помощью JavaScriptExecutor")
@allure.title("Загрузка страницы с Registration Form")
@allure.description(
    """
    Цель: Проверить работу JavaScriptExecutor

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Проверить наличие скролла на странице

    Ожидаемый результат:
        - Определение наличия скролла на странице""")
def test_page_has_scroll(browser: fixture):
    registration_page = RegistrationPage(browser)
    registration_page.open_form_page()
    registration_page.assert_page_scroll()

