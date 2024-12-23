import allure
from allure import severity_level
from pytest import fixture

from pages import TabsPage


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Tabs")
@allure.testcase("Задача U11")
@allure.story("Нажать на ссылку, перейти в новую вкладку")
@allure.title("Переход по ссылке на новую вкладку")
@allure.description(
    """
    Цель: Проверить переход по открытые вкладки

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу
        2. Переключиться на iframe
        3. Нажать на ссылку
        4. Проверить, что новая вкладка открылась
        5. Перейти на новую вкладку
        6. Нажать на ссылку
        7. Проверить, что новая вкладка открылась

    Ожидаемый результат:
        - После двух нажатий на ссылку открыто три вкладки""")
def test_tabs(browser: fixture):
    tabs_page = TabsPage(browser)
    tabs_page.open_page()
    tabs_page.switch_to_iframe()
    tabs_page.click_link()
    two_tabs_window = tabs_page.get_current_window_handles()
    with allure.step('Проверить, что новая вкладка открылась'):
        assert len(two_tabs_window) == 2, 'Expected second tab opened'
    tabs_page.switch_to_new_tab(two_tabs_window[-1])
    tabs_page.click_link()
    with allure.step('Проверить, что новая вкладка открылась'):
        assert len(tabs_page.get_current_window_handles()) == 3, 'Expected third tab opened'


