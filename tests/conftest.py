import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()
