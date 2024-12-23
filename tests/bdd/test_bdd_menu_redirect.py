import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then
from pages import Menu


scenarios('./features/menu_redirect.feature')


@pytest.fixture
def menu_redirect(browser: fixture):
    return Menu(browser)


@given('Homepage')
def open_page(menu_redirect: fixture):
    menu_redirect.open_homepage()


@when('Click on menu item "Appium"')
def click_menu_item(menu_redirect: fixture):
    menu_redirect.hover_over_all_courses()
    menu_redirect.click_appium()


@when('Click on menu item "Appium with Python"')
def click_menu_item(menu_redirect: fixture):
    menu_redirect.click_appium_python()


@then('Redirection to the "Appium with Python" page successful')
def click_menu_item(menu_redirect: fixture):
    menu_redirect.assert_redirection_to_appium_python()
    menu_redirect.check_page_title("Appium Python Online Training in USA, India | Way2Automation")
    menu_redirect.appium_python_elements_are_active()


@when('Click on menu item "Spring Boot"')
def click_menu_item(menu_redirect: fixture):
    menu_redirect.hover_over_video_tutorial()
    menu_redirect.click_spring_boot()


@then('Redirection to the "Spring Boot" page successful')
def click_menu_item(menu_redirect: fixture):
    menu_redirect.assert_redirection_to_spring_boot()
    menu_redirect.check_page_title("Spring Boot with complete Bootcamp | Way2Automation")
    menu_redirect.spring_boot_elements_are_active()
