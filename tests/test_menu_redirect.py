import allure
from allure import severity_level
from pytest import fixture

from pages import Menu


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Переход на страницу по ссылке")
@allure.testcase("Задача U1, U2")
@allure.story("Переход по ссылке проходит успешно, основные элементы новой страницы отображаются корректно")
@allure.title("Переход по меню на другие страницы")
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
        5. Проверить переход на страницу
        6. Проверить значение "TITLE"
        7. Проверить корректность отображения элементов страницы

    Ожидаемый результат:
        - Происходит переход на страницу
        - Значение "TITLE" соответствует странице
        - Элементы, уникальные для этой страницы, активны""")
def test_redirect_to_appium_python(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_all_courses()
    menu.click_appium()
    menu.click_appium_python()
    menu.assert_redirection_to_appium_python()
    menu.check_page_title("Appium Python Online Training in USA, India | Way2Automation")
    menu.appium_python_elements_are_active()


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Переход на страницу по ссылке")
@allure.testcase("Задача U1, U2")
@allure.story("Переход по ссылке проходит успешно, основные элементы новой страницы отображаются корректно")
@allure.title("Переход по меню на другие страницы")
@allure.description(
    """
    Цель: Проверка перехода по меню на другие страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Навести курсор на вкладку меню "Video Tutorial"
        3. Кликнуть пункт "Spring Boot"
        4. Проверить переход на страницу
        5. Проверить значение "TITLE"
        6. Проверить корректность отображения элементов страницы

    Ожидаемый результат:
        - Происходит переход на страницу
        - Значение "TITLE" соответствует странице
        - Элементы, уникальные для этой страницы, активны""")
def test_redirect_to_video_tutorial_spring(browser: fixture):
    menu = Menu(browser)
    menu.open_homepage()
    menu.hover_over_video_tutorial()
    menu.click_spring_boot()
    menu.assert_redirection_to_spring_boot()
    menu.check_page_title("Spring Boot with complete Bootcamp | Way2Automation")
    menu.spring_boot_elements_are_active()
