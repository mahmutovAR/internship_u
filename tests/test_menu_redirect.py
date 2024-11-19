from pytest import fixture

from pages import Menu


def test_menu_redirect(browser: fixture):
    """Checks redirection from menu by link."""
    menu = Menu(browser)
    menu.go_to_homepage()
    menu.check_link_all_courses_appium_python()
    menu.check_link_video_tutorial_spring()
    menu.check_resources_site_1()
    menu.check_resources_blog()
