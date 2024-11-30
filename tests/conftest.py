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
    options.add_argument("--window-size=1920x1080")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
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
