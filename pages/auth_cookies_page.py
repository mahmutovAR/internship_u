import pickle
from os.path import abspath, dirname, isfile
from os.path import join as os_path_join

import allure

from data import PageUrls
from locators import AuthCookiesLocators
from . import BasePage


class AuthCookiesPage(BasePage):
    def open_login_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(PageUrls.auth_cookies)

    def fill_login(self, login: str) -> None:
        with allure.step('Ввести данные в поле "Login"'):
            self.send_keys_to_element(AuthCookiesLocators.login, login)

    def fill_password(self, password: str) -> None:
        with allure.step('Ввести данные в поле "Password"'):
            self.send_keys_to_element(AuthCookiesLocators.password, password)

    def click_enter_button(self) -> None:
        with allure.step('Кликнуть кнопку "Enter"'):
            self.click_element(AuthCookiesLocators.enter_button)

    def get_and_save_cookies(self) -> None:
        with allure.step('Сохранить cookies в файл'):
            cookies = self.get_cookies_data()
            with open("cookies.pkl", "wb") as cookies_file:
                pickle.dump(cookies, cookies_file)

    @staticmethod
    def assert_cookies_file_exists() -> None:
        with allure.step('Проверить, что файл с cookies создан'):
            cookies_file_path = os_path_join(dirname(abspath(__file__)), 'cookies.pkl')
            assert isfile(cookies_file_path), 'Cookies file expected to be created'

    def load_cookies(self) -> None:
        with allure.step('Загрузить cookies из файла'):
            with open("cookies.pkl", "rb") as cookies_file:
                self.load_cookies_data(pickle.load(cookies_file))
