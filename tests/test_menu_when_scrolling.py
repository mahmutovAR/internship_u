from pytest import fixture

from pages import Menu


def test_menu_when_scrolling(browser: fixture):
    """Checks that menu elements are present when scrolling the page."""
    menu = Menu(browser)
    menu.go_to_homepage()
    menu.menu_items_are_clickable_when_scrolling()
