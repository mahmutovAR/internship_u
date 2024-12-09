import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


pytest_plugins = 'tests.fixtures'


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    hub_url = "http://localhost:4444/wd/hub"
    driver = webdriver.Remote(command_executor=hub_url, options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        driver = item.funcargs.get('browser')
        if driver:
            with allure.step('Скриншот упавшего теста'):
                allure.attach(driver.get_screenshot_as_png(),
                              name='Test failure screenshot',
                              attachment_type=AttachmentType.PNG)
