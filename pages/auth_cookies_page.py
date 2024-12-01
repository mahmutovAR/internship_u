import allure

from data import PageUrls
from locators import AuthCookiesLocators
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

    def delete_cookies(self) -> None:
        with allure.step('Удалить cookies'):
            self.delete_cookies_data()
