import allure
from selenium.webdriver.support.ui import Select

from data import PageUrls
from locators import RegistrationLocators
from . import BasePage


class RegistrationPage(BasePage):
    def open_form_page(self) -> None:
        with allure.step('Открыть страницу с формой'):
            self.open_url(PageUrls.registration_page)

    def select_list_value(self, list_locator: tuple[str, str], value: str) -> None:
        select = Select(self.get_element_by_locator(list_locator))
        select.select_by_value(value)

    def fill_first_name(self, first_name: str) -> None:
        with allure.step('Заполнить поле "First Name"'):
            self.send_keys_to_element(RegistrationLocators.first_name, first_name)

    def fill_last_name(self, last_name: str) -> None:
        with allure.step('Заполнить поле "Last Name"'):
            self.send_keys_to_element(RegistrationLocators.last_name, last_name)

    def select_marital_status(self, marital_status: str) -> None:
        with allure.step('Выбрать "Marital Status"'):
            if marital_status.lower() == 'single':
                self.click_element(RegistrationLocators.marital_status_single)
            elif marital_status.lower() == 'married':
                self.click_element(RegistrationLocators.marital_status_married)
            elif marital_status.lower() == 'divorced':
                self.click_element(RegistrationLocators.marital_status_divorced)
            else:
                assert False, 'Invalid "Marital status"'

    def select_hobby(self, hobby: list) -> None:
        with allure.step('Выбрать "Hobby"'):
            if 'dance' in hobby:
                self.click_element(RegistrationLocators.hobby_dance)
            if 'reading' in hobby:
                self.click_element(RegistrationLocators.hobby_reading)
            if 'cricket' in hobby:
                self.click_element(RegistrationLocators.hobby_cricket)

    def select_country(self, country: str) -> None:
        with allure.step('Выбрать "Country" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.country, country)

    def select_birth_month(self, month: str) -> None:
        with allure.step('Выбрать "Month" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_month, month)

    def select_birth_day(self, day: str) -> None:
        with allure.step('Выбрать "Day" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_day, day)

    def select_birth_year(self, year: str) -> None:
        with allure.step('Выбрать "Year" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_year, year)

    def fill_phone(self, phone: str) -> None:
        with allure.step('Заполнить поле "Phone Number"'):
            self.send_keys_to_element(RegistrationLocators.phone, phone)

    def fill_username(self, username: str) -> None:
        with allure.step('Заполнить поле "Username"'):
            self.send_keys_to_element(RegistrationLocators.username, username)

    def fill_email(self, email: str) -> None:
        with allure.step('Заполнить поле "E-mail"'):
            self.send_keys_to_element(RegistrationLocators.email, email)

    def choose_picture(self, picture: str) -> None:
        with allure.step('Загрузить изображение в поле "Your Profile Picture"'):
            self.send_keys_to_element(RegistrationLocators.picture, picture)

    def fill_about(self, about: str) -> None:
        with allure.step('Заполнить поле "About Yourself"'):
            self.send_keys_to_element(RegistrationLocators.about, about)

    def fill_password(self, password: str) -> None:
        with allure.step('Заполнить поле "Password"'):
            self.send_keys_to_element(RegistrationLocators.password, password)

    def fill_confirm_password(self, confirm_password: str) -> None:
        with allure.step('Заполнить поле "Confirm Password"'):
            self.send_keys_to_element(RegistrationLocators.confirm_password, confirm_password)

    def submit_data(self) -> None:
        with allure.step('Нажать на кнопку "SUBMIT"'):
            self.click_element(RegistrationLocators.submit_button)

    def no_error_found(self) -> None:
        with allure.step('Проверить отсутствие сообщений об ошибках'):
            assert not self.element_is_visible(RegistrationLocators.error), 'Expected that no error message are displayed'

    def click_first_name_field(self) -> None:
        with allure.step('Кликнуть поле ввода "First Name"'):
            self.click_element(RegistrationLocators.first_name)

    def assert_focus_on_element(self) -> None:
        with allure.step('Проверить, что фокус на поле ввода'):
            assert self.get_element_by_locator(RegistrationLocators.first_name) == self.get_active_element(), 'Excepted element is active'

    def blur_first_name_field(self) -> None:
        with allure.step('Убрать фокус из поля ввода с помощью JavaScriptExecutor'):
            self.blur_element(RegistrationLocators.first_name)

    def assert_element_not_active(self) -> None:
        with allure.step('Проверить, что поле ввода не в фокусе'):
            assert self.get_element_by_locator(RegistrationLocators.first_name) != self.get_active_element(), 'Excepted element is not active'

    def assert_page_scroll(self) -> None:
        with allure.step('Проверить наличие скролла на странице'):
            assert self.page_has_scroll(), 'Expected page has scroll'
