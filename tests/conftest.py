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


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_makereport(item, call):
    if call.excinfo is not None:
        driver = item.funcargs.get('browser')
        take_screenshot(driver, 'Скриншот упавшего теста', 'Test failure screenshot')

    elif call.when == 'call':
        driver = item.funcargs.get('browser')
        take_screenshot(driver, 'Скриншот пройденного теста', 'Test passed screenshot')


def take_screenshot(driver: webdriver, allure_step: str, name: str):
    if driver:
        with allure.step(allure_step):
            allure.attach(driver.get_screenshot_as_png(),
                          name=name,
                          attachment_type=AttachmentType.PNG)
