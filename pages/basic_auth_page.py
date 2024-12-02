import allure

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

    # def switch_to_iframe(self) -> None:
    #     self.switch_to_iframe_by_locator(AlertsLocators.iframe)

    def enter_login_and_password(self, login: str, password: str) -> None:
        with allure.step('Ввести логин и пароль"'):
            self.enter_login_and_password_to_alert(login, password)

    def assert_authorization(self) -> None:
        with allure.step('Проверить, что авторизация прошла успешно'):
            pass
