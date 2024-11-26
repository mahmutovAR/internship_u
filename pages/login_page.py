import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from data import URL
from locators import LoginLocators
from . import BasePage


class LoginPage(BasePage):
    def open_login_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(URL.login_page)

    def get_field_label(self, field_locator: tuple[str, str]) -> str:
        self.element_is_clickable(field_locator)
        label_locator = (By.XPATH, f"{field_locator[1]}/preceding-sibling::label")
        return self.get_element_by_locator(label_locator).text

    def find_username_field(self) -> str:
        with allure.step('Проверить наличие поля ввода "Username"'):
            return self.get_field_label(LoginLocators.username)

    def find_password_field(self) -> str:
        with allure.step('Проверить наличие поля ввода "Password"'):
            return self.get_field_label(LoginLocators.password)

    def find_username_desc_field(self) -> str:
        with allure.step('Проверить наличие поля ввода "Username *"'):
            return self.get_field_label(LoginLocators.username_desc)

    def click_username_field(self) -> None:
        with allure.step('Кликнуть поле ввода "Username"'):
            self.click_element(LoginLocators.username)

    def click_password_field(self) -> None:
        with allure.step('Кликнуть поле ввода "Password"'):
            self.click_element(LoginLocators.password)

    def click_username_desc_field(self) -> None:
        with allure.step('Кликнуть поле ввода "Username *"'):
            self.click_element(LoginLocators.username_desc)

    def click_somewhere(self) -> None:
        with allure.step('Кликнуть в пустую часть страницы'):
            self.click_element((By.TAG_NAME, "body"))

    def check_username_error(self) -> WebElement:
        return self.get_element_by_locator(LoginLocators.username_err)

    def check_password_error(self) -> WebElement:
        return self.get_element_by_locator(LoginLocators.password_err)

    def check_username_desc_color(self) -> str:
        return self.get_element_by_locator(LoginLocators.username_desc_err).value_of_css_property('color')

    def check_login_button_is_enabled(self) -> bool:
        return self.get_element_by_locator(LoginLocators.login_button).is_enabled()

    def fill_username(self, username: str) -> None:
        with allure.step('Ввести данные в поле "Username"'):
            self.send_keys_to_element(LoginLocators.username, username)

    def fill_password(self, password: str) -> None:
        with allure.step('Ввести данные в поле "Password"'):
            self.send_keys_to_element(LoginLocators.password, password)

    def fill_username_desc(self, username_desc: str) -> None:
        with allure.step('Ввести данные в поле "Username *"'):
            self.send_keys_to_element(LoginLocators.username_desc, username_desc)

    def click_login_button(self) -> None:
        with allure.step('Кликнуть кнопку "Login"'):
            self.click_element(LoginLocators.login_button)

    def assert_auth_success(self) -> str:
        return self.get_element_by_locator(LoginLocators.auth_success).text

    def assert_auth_error(self) -> str:
        return self.get_element_by_locator(LoginLocators.auth_error).text

    def click_logout_button(self) -> None:
        with allure.step('Кликнуть кнопку "Logout"'):
            self.click_element(LoginLocators.logout_link)

    def find_username_desc_field_after_logout(self) -> str:
        with allure.step('Проверить наличие поля ввода "Username *"'):
            return self.get_field_label(LoginLocators.username_desc_2)
