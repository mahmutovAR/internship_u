import allure
import pytest
from allure_commons.types import AttachmentType

from helpers.driver_factory import DriverFactory


pytest_plugins = 'tests.fixtures'


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("--browser").lower()
    grid = request.config.getoption("--grid")
    driver = DriverFactory(browser_name, grid).get_driver()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--grid", action="store_true", default=False)


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        driver = item.funcargs.get('browser')
        if driver:
            with allure.step('Скриншот упавшего теста'):
                allure.attach(driver.get_screenshot_as_png(),
                              name='Test failure screenshot',
                              attachment_type=AttachmentType.PNG)
