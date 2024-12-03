import allure
import requests
from requests.auth import HTTPBasicAuth

from data import PageUrls
from locators import BasicAuthLocators
from . import BasePage


class BasicAuthPage(BasePage):
    def open_page(self) -> None:
        with allure.step('Открыть страницу'):
            self.open_url(PageUrls.basic_auth_page)

    def click_display_image(self) -> None:
        with allure.step('Нажать "Display Image"'):
            self.click_element(BasicAuthLocators.display_image)

    @staticmethod
    def log_in(username: str, password: str) -> int:
        with allure.step('Авторизироваться с корректными "username" и "password"'):
            response = requests.get(PageUrls.basic_auth_page, auth=HTTPBasicAuth(username, password))
            return response.status_code
