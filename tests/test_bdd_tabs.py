import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then

from pages import TabsPage


scenarios('./features/tabs.feature')


@pytest.fixture
def tabs(browser: fixture):
    return TabsPage(browser)


@given('Tabs page')
def open_page(tabs: fixture):
    tabs.open_page()


@when('Click link')
def click_tab_link(tabs: fixture):
    tabs.switch_to_iframe()
    tabs.click_link()


@then('New tab opened')
def check_tab_opened(tabs: fixture, data_storage: fixture):
    two_tabs_window = tabs.get_current_window_handles()
    assert len(two_tabs_window) == 2, 'Expected second tab opened'
    data_storage['tabs_window'] = two_tabs_window


@when('Click second link')
def click_tab_link(tabs: fixture, data_storage: fixture):
    tabs.switch_to_new_tab(data_storage['tabs_window'][-1])
    tabs.click_link()


@then('Three tabs are opened')
def check_tabs_opened(tabs: fixture):
    assert len(tabs.get_current_window_handles()) == 3, 'Expected third tab opened'
