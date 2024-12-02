import allure
from allure import severity_level
from pytest import fixture

from pages import AlertsPage


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Alert input")
@allure.testcase("Задача U12")
@allure.story("""Нажать "Input Alert", ввести текст""")
@allure.title("Ввод текста в всплывающем окно")
@allure.description(
    """
    Цель: Проверить ввод текста в всплывающем окно

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу
        2. Нажать "Input Alert"
        3. Нажать кнопку для вызова "Input box"
        4. Ввести текст
        5. Проверить, что текст применился

    Ожидаемый результат:
        - После ввода в всплывающем окне, текст отображается на странице""")
def test_alert_input(browser: fixture, alerts_form_data: fixture):
    alerts_page = AlertsPage(browser)
    alerts_page.open_page()
    alerts_page.click_input_alert()
    alerts_page.switch_to_iframe()
    alerts_page.click_input_box()
    data = alerts_form_data
    name = f'{data.first_name} {data.last_name}'
    alerts_page.input_text(name)
    expected = f'Hello {name}! How are you today?'
    with allure.step('Проверить, что текст применился'):
        text = alerts_page.get_text()
        assert text == expected, f'Expected "{expected}" to be displayed, but got "{text}"'
