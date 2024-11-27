import allure
from allure import severity_level
from pytest import fixture

from pages import Menu


@allure.severity(severity_level.NORMAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка перехода на другие страницы")
@allure.description(
    """
    Цель: Проверка перехода по меню на другие страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Навести курсор на вкладку меню "All Courses"
        3. Кликнуть пункт "Appium"
        4. Кликнуть пункт "Appium with Python"

    Ожидаемый результат:
        - Происходит переход на соответствующую страницу
        - Элементы, уникальные для этой страницы, активны""")
def test_redirect_to_appium_python(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_all_courses()
    menu.click_appium()
    menu.click_appium_python()
    menu.assert_redirection_to_appium_python()
    menu.appium_python_elements_are_active()


@allure.severity(severity_level.NORMAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка перехода на другие страницы")
@allure.description(
    """
    Цель: Проверка перехода по меню на другие страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Навести курсор на вкладку меню "Video Tutorial"
        3. Кликнуть пункт "Spring Boot"

    Ожидаемый результат:
        - Происходит переход на соответствующую страницу
        - Элементы, уникальные для этой страницы, активны""")
def test_redirect_to_video_tutorial_spring(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_video_tutorial()
    menu.click_spring_boot()
    menu.assert_redirection_to_spring_boot()
    menu.spring_boot_elements_are_active()
