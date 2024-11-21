from pytest import fixture

from pages import Menu


def test_menu_redirect(browser: fixture):
    """Checks redirection from menu by link.
    3. Проверка перехода по меню на другие страницы
    - Пример: перейти на страницу Resources -> Practice Site1.
    - Проверить, что страница загружается корректно и все основные элементы (шапка, меню, контент) отображаются."""
    menu = Menu(browser)
    menu.get_homepage()
    menu.check_link_all_courses_appium_python()
    menu.check_link_video_tutorial_spring()
    menu.check_resources_site_1()
    menu.check_resources_blog()
