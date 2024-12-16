import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then
from pages import Menu


scenarios('./features/menu_when_scrolling.feature')


@pytest.fixture
def menu(browser: fixture):
    return Menu(browser)


@given('Homepage')
def open_page(menu: fixture):
    menu.open_homepage()


@when('Scroll to Footer')
def click_menu_item(menu: fixture):
    menu.scroll_to_footer()


@then('All Menu items are present and clickable')
def check_menu(menu: fixture):
    menu.menu_items_are_visible_and_clickable()
