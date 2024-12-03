import allure

from data import PageUrls
from locators import BasicAuthLocators
from . import BasePage


class BasicAuthPage(BasePage):
    def open_page(self, username: str, password: str) -> None:
        with allure.step('Открыть страницу'):
            domain = PageUrls.basic_auth_page.split('://')[1]
            url = f'https://{username}:{password}@{domain}'
            self.open_url(url)

    def click_display_image(self) -> None:
        with allure.step('Нажать "Display Image"'):
            self.click_element(BasicAuthLocators.display_image)

    def auth_image_is_visible(self) -> bool:
        return self.element_is_visible(BasicAuthLocators.auth_image)
