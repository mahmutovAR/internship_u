import allure
from selenium.webdriver.common.by import By

from data import PageUrls
from locators import LoginLocators
from . import BasePage


class LoginPage(BasePage):
    def open_login_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(PageUrls.login_page)

    def get_field_label(self, field_locator: tuple[str, str]) -> str:
        self.get_clickable_element(field_locator)
        label_locator = (By.XPATH, f"{field_locator[1]}/preceding-sibling::label")
        return self.get_element_by_locator(label_locator).text

    def check_username_field_label(self) -> None:
        with allure.step('Проверить наличие поля ввода "Username"'):
            assert self.element_is_visible(LoginLocators.username), 'Expected field "Username" is enable'
            username_label = self.get_field_label(LoginLocators.username)
            assert username_label == 'Username', f'Expected label is "Username", but got {username_label}'

    def check_password_field_label(self) -> None:
        with allure.step('Проверить наличие поля ввода "Password"'):
            assert self.element_is_visible(LoginLocators.password), 'Expected field "Username" is enable'
            password_label = self.get_field_label(LoginLocators.password)
            assert password_label == 'Password', f'Expected label is "Password", but got {password_label}'

    def check_username_desc_field_label(self) -> None:
        with allure.step('Проверить наличие поля ввода "Username *"'):
            assert self.element_is_visible(LoginLocators.username_desc), 'Expected field "Username" is enable'
            username_desc_label = self.get_field_label(LoginLocators.username_desc)
            assert username_desc_label == 'Username *', f'Expected label is "Username *", but got {username_desc_label}'

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

    def check_username_error(self) -> None:
        with allure.step('Проверить сообщение с ошибкой незаполненного поля "Username"'):
            username_label = self.get_element_text(LoginLocators.username_err)
            assert username_label == 'You did not enter a username', f'Expected error message "You did not enter a username", but got {username_label}'

    def check_password_error(self) -> None:
        with allure.step('Проверить сообщение с ошибкой незаполненного поля "Password"'):
            password_label = self.get_element_text(LoginLocators.password_err)
            assert password_label == 'You did not enter a username', f'Expected error message "You did not enter a username", but got {password_label}'

    def check_username_desc_error(self) -> None:
        with allure.step('Проверить цвет описания поля "Username *"'):
            expected_color = 'rgba(169, 68, 66, 1)'  # RGB value for #a94442
            field_color = self.get_element_by_locator(LoginLocators.username_desc_err).value_of_css_property('color')
            assert field_color == expected_color, f'Expected "Username *" field changes color to {expected_color}, but got {field_color}'

    def check_login_button_is_not_enabled(self) -> None:
        with allure.step('Проверить, что кнопка "Login" не активна'):
            assert not self.get_element_by_locator(LoginLocators.login_button).is_enabled()

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

    def assert_auth_success(self) -> None:
        with allure.step('Проверить, что отображается сообщение об успешной авторизации'):
            expected_message = "You're logged in!!"
            auth_message = self.get_element_text(LoginLocators.auth_success)
            assert auth_message == expected_message, f'Expected {expected_message} message, but got {auth_message}'

    def assert_auth_error(self) -> None:
        with allure.step('Проверить, что отображается сообщение о ошибке авторизации'):
            expected_message = "Username or password is incorrect"
            auth_message = self.get_element_text(LoginLocators.auth_error)
            assert auth_message == expected_message, f'Expected {expected_message} message, but got {auth_message}'

    def assert_field_error(self, username_error: bool, password_error: bool, username_desc_error: bool) -> None:
        with allure.step('Проверить, что отображаются сообщения о некорректном вводе'):
            username_error_message = "Your username must be between 3 and 50 characters long"
            password_error_message = "Your username must be between 3 and 100 characters long"
            if username_error:
                username_label = self.get_element_text(LoginLocators.username_err)
                assert username_label == username_error_message, f'Expected error message "{username_error_message}", but got {username_label}'

            if password_error:
                password_label = self.get_element_text(LoginLocators.password_err)
                assert password_label == password_error_message, f'Expected error message "{password_error_message}", but got {password_label}'

            if username_desc_error:
                expected_color = 'rgba(169, 68, 66, 1)'  # RGB value for #a94442
                field_color = self.get_element_by_locator(LoginLocators.username_desc_err).value_of_css_property(
                    'color')
                assert field_color == expected_color, f'Expected "Username *" field changes color to {expected_color}, but got {field_color}'

    def click_logout_button(self) -> None:
        with allure.step('Кликнуть кнопку "Logout"'):
            self.click_element(LoginLocators.logout_link)

    def check_username_desc_field_label_after_logout(self) -> None:
        with allure.step('Проверить наличие поля ввода "Username *"'):
            username_desc_label = self.get_field_label(LoginLocators.username_desc_2)
            assert username_desc_label == 'Username *', f'Expected label is "Username *", but got {username_desc_label}'
