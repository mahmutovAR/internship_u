import allure
from selenium.webdriver.support.ui import Select

from data import URL
from locators import RegistrationLocators
from . import BasePage


class RegistrationPage(BasePage):
    def open_form_page(self):
        with allure.step('Открыть страницу с формой'):
            self.open_url(URL.registration_page)

    def fill_in_field(self, field_locator: tuple[str, str], data: str):
        self.send_keys_to_element(field_locator, data)

    def select_list_value(self, list_locator: tuple[str, str], value: str):
        select = Select(self.get_element_by_locator(list_locator))
        select.select_by_value(value)

    def fill_first_name(self, first_name: str):
        with allure.step('Заполнить поле "First Name"'):
            self.fill_in_field(RegistrationLocators.first_name, first_name)

    def fill_last_name(self, last_name: str):
        with allure.step('Заполнить поле "Last Name"'):
            self.fill_in_field(RegistrationLocators.last_name, last_name)

    def select_marital_status(self, marital_status: str):
        with allure.step('Выбрать "Marital Status"'):
            if marital_status.lower() == 'single':
                self.click_element(RegistrationLocators.marital_status_single)
            elif marital_status.lower() == 'married':
                self.click_element(RegistrationLocators.marital_status_married)
            elif marital_status.lower() == 'divorced':
                self.click_element(RegistrationLocators.marital_status_divorced)
            else:
                assert False, 'Invalid "Marital status"'

    def select_hobby(self, hobby: list):
        with allure.step('Выбрать "Hobby"'):
            if 'dance' in hobby:
                self.click_element(RegistrationLocators.hobby_dance)
            if 'reading' in hobby:
                self.click_element(RegistrationLocators.hobby_reading)
            if 'cricket' in hobby:
                self.click_element(RegistrationLocators.hobby_cricket)

    def select_country(self, country: str):
        with allure.step('Выбрать "Country" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.country, country)

    def select_birth_month(self, month: str):
        with allure.step('Выбрать "Month" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_month, month)

    def select_birth_day(self, day: str):
        with allure.step('Выбрать "Day" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_day, day)

    def select_birth_year(self, year: str):
        with allure.step('Выбрать "Year" поля "Date of Birth" из выпадающего списка'):
            self.select_list_value(RegistrationLocators.date_of_birth_year, year)

    def fill_phone(self, phone: str):
        with allure.step('Заполнить поле "Phone Number"'):
            self.fill_in_field(RegistrationLocators.phone, phone)

    def fill_username(self, username: str):
        with allure.step('Заполнить поле "Username"'):
            self.fill_in_field(RegistrationLocators.username, username)

    def fill_email(self, email: str):
        with allure.step('Заполнить поле "E-mail"'):
            self.fill_in_field(RegistrationLocators.email, email)

    def choose_picture(self, picture: str):
        with allure.step('Загрузить изображение в поле "Your Profile Picture"'):
            self.send_keys_to_element(RegistrationLocators.picture, picture)

    def fill_about(self, about: str):
        with allure.step('Заполнить поле "About Yourself"'):
            self.fill_in_field(RegistrationLocators.about, about)

    def fill_password(self, password: str):
        with allure.step('Заполнить поле "Password"'):
            self.fill_in_field(RegistrationLocators.password, password)

    def fill_confirm_password(self, confirm_password: str):
        with allure.step('Заполнить поле "Confirm Password"'):
            self.fill_in_field(RegistrationLocators.confirm_password, confirm_password)

    def submit_data(self):
        with allure.step('Submit data'):
            self.click_element(RegistrationLocators.submit_button)

    def no_error_found(self):
        assert not self.element_is_visible(RegistrationLocators.error), 'Expected that no error message are displayed'
