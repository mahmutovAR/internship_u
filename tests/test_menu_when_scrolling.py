import allure
from allure import severity_level
from pytest import fixture

from pages import Menu


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка поведения основного меню")
@allure.description(
    """
    Цель: Проверка поведения основного меню в шапке при скроллинге

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть домашнюю страницу
         2. Прокрутить страницу до блока "Footer"

    Ожидаемый результат:
        - Все основные пункты меню отображаются и кликабельны""")
def test_menu_when_scrolling(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.scroll_to_footer()
    menu.menu_items_are_visible_and_clickable()
