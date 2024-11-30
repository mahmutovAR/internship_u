import allure

from data import PageUrls
from locators import AuthCookiesLocators
from tests.cookie_helper import CookieHelper
from . import BasePage


cookie_helper = CookieHelper()


class AuthCookiesPage(BasePage):
    def open_auth_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(PageUrls.auth_cookies_page)

    def check_auth_form(self) -> None:
        with allure.step('Проверить, что доступны поля авторизации'):
            self.element_is_visible(AuthCookiesLocators.login)
            self.element_is_visible(AuthCookiesLocators.password)
            self.element_is_visible(AuthCookiesLocators.enter_button)
            self.element_is_visible(AuthCookiesLocators.enter_without_login)

    def click_enter_without_login_button(self) -> None:
        with allure.step('Кликнуть кнопку "Enter without login"'):
            self.click_element(AuthCookiesLocators.enter_without_login)

    def check_guest_authentication(self) -> None:
        with allure.step('Проверить, что авторизация прошла под именем "guest"'):
            text = self.get_element_text(AuthCookiesLocators.guest_auth)
            assert text.endswith('guest'), 'Expected Guest authentication to be successful'

    def click_logout_button(self) -> None:
        with allure.step('Кликнуть кнопку "logout"'):
            self.click_element(AuthCookiesLocators.logout_button)

    def save_cookies_to_file(self) -> None:
        with allure.step('Сохранить cookies в файл'):
            cookie_helper.save_cookies_to_file(self.get_cookies_data())

    @staticmethod
    def assert_cookies_file_exists() -> None:
        with allure.step('Проверить, что файл с cookies создан'):
            assert cookie_helper.file_exists(), 'Cookies file expected to be created'

    def delete_cookies(self) -> None:
        with allure.step('Удалить cookies'):
            self.delete_cookies_data()

    def load_cookies_from_file(self) -> None:
        with allure.step('Загрузить cookies из файла'):
            self.load_cookies_data(cookie_helper.load_cookies_from_file())

    @staticmethod
    def delete_cookies_file() -> None:
        with allure.step('Удалить файл с cookies'):
            cookie_helper.delete_cookies_file()
            assert not cookie_helper.file_exists(), 'Cookies file expected to be deleted'
