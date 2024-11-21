import pytest
from selenium import webdriver
import allure
from allure_commons.types import AttachmentType

pytest_plugins = 'tests.fixtures'


@pytest.fixture(scope="function")
def browser():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        browser = item.funcargs.get('browser')
        if browser:
            with allure.step('Take screenshot of test failure'):
                allure.attach(browser.get_screenshot_as_png(),
                              name="Test failure screenshot",
                              attachment_type=AttachmentType.PNG)
