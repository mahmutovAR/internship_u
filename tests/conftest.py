import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


pytest_plugins = 'tests.fixtures'


@pytest.fixture(scope="function")
def browser():
    options = Options()
    options.add_argument("--headless")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1600, 1200)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def browser_with_window():
    driver = webdriver.Chrome()
    driver.set_window_size(1600, 1200)
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
        driver_2 = item.funcargs.get('browser_with_window')
        if driver_2:
            with allure.step('Скриншот упавшего теста'):
                allure.attach(driver_2.get_screenshot_as_png(),
                              name='Test failure screenshot',
                              attachment_type=AttachmentType.PNG)
