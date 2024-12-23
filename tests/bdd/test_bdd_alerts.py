import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers

from pages import AlertsPage

scenarios('./features/alerts.feature')


@pytest.fixture
def alerts(browser: fixture):
    return AlertsPage(browser)


@given('Alerts page')
def alerts_open_page(alerts: fixture):
    alerts.open_page()


@when('Click "Input Alert"')
def alerts_click_input_alert(alerts: fixture):
    alerts.click_input_alert()


@when('click button to activate "Input box"')
def alerts_click_input_box(alerts: fixture):
    alerts.switch_to_iframe()
    alerts.click_input_box()


@when(parsers.parse('enter text "{name}"'))
def alerts_input_text(alerts: fixture, name: str, data_storage: fixture):
    alerts.input_text(name)
    data_storage['name'] = name


@then('Entered text is displayed')
def alerts_check_text(alerts: fixture, data_storage: fixture):
    expected = f'Hello {data_storage['name']}! How are you today?'
    text = alerts.get_text()
    assert text == expected, f'Expected "{expected}" to be displayed, but got "{text}"'
