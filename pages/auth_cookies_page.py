import allure

from data import PageUrls
from locators import AuthCookiesLocators, AltAuthCookiesLocators
from . import BasePage


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

    def fill_username(self, username: str) -> None:
        with allure.step('Ввести данные в поле "Username"'):
            self.send_keys_to_element(AuthCookiesLocators.login, username)

    def fill_password(self, password: str) -> None:
        with allure.step('Ввести данные в поле "Password"'):
            self.send_keys_to_element(AuthCookiesLocators.password, password)

    def click_login(self) -> None:
        with allure.step('Кликнуть кнопку "Enter"'):
            self.click_element(AuthCookiesLocators.enter_button)

    def check_guest_authentication(self) -> None:
        with allure.step('Проверить, что авторизация прошла под именем "guest"'):
            text = self.get_element_text(AuthCookiesLocators.guest_auth)
            assert text.endswith('guest'), 'Expected "Guest authentication" to be successful'

    def click_logout_button(self) -> None:
        with allure.step('Кликнуть кнопку "logout"'):
            self.click_element(AuthCookiesLocators.logout_button)

    def delete_cookies(self) -> None:
        with allure.step('Удалить cookies'):
            self.delete_cookies_data()


class AltAuthCookiesPage(BasePage):
    def open_auth_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(PageUrls.alt_auth_cookies_page)

    def check_auth_form(self) -> None:
        with allure.step('Проверить, что доступны поля авторизации'):
            self.element_is_visible(AltAuthCookiesLocators.username)
            self.element_is_visible(AltAuthCookiesLocators.password)
            self.element_is_visible(AltAuthCookiesLocators.login)

    def fill_username(self, username: str) -> None:
        with allure.step('Ввести данные в поле "Username"'):
            self.send_keys_to_element(AltAuthCookiesLocators.username, username)

    def fill_password(self, password: str) -> None:
        with allure.step('Ввести данные в поле "Password"'):
            self.send_keys_to_element(AltAuthCookiesLocators.password, password)

    def click_login(self) -> None:
        with allure.step('Кликнуть кнопку "Login"'):
            self.click_element(AltAuthCookiesLocators.login)

    def check_authorization(self) -> bool:
        return self.element_is_visible(AltAuthCookiesLocators.auth_message)

    def click_logout(self) -> None:
        with allure.step('Кликнуть кнопку "Logout"'):
            self.click_element(AltAuthCookiesLocators.logout)

    def open_logged_page(self) -> None:
        with allure.step('Открыть страницу успешной авторизации'):
            self.open_url(PageUrls.alt_auth_cookies_logged_page)

    def delete_cookies(self) -> None:
        with allure.step('Удалить cookies'):
            self.delete_cookies_data()
