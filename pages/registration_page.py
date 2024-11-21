from os import environ
from os.path import join as os_path_join
from pathlib import Path

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from locators import RegistrationLocators
from . import BasePage


class RegistrationPage(BasePage):

    def go_to_form_page(self):
        with allure.step('Open "Registration Form" url'):
            self.get_registration_page()
            self.wait_for_visibility(RegistrationLocators.form)

    def fill_in_field(self, field_locator: tuple[str, str], data: str):
        self.get_element_by_locator(field_locator).send_keys(data)

    def select_marital_status(self, marital_status: str):
        if marital_status.lower() == 'single':
            self.get_element_by_locator(RegistrationLocators.marital_status_single).click()
        elif marital_status.lower() == 'married':
            self.get_element_by_locator(RegistrationLocators.marital_status_married).click()
        elif marital_status.lower() == 'divorced':
            self.get_element_by_locator(RegistrationLocators.marital_status_divorced).click()
        else:
            assert False, 'Invalid "Marital status"'

    def select_hobby(self, hobby: list):
        if 'dance' in hobby:
            self.get_element_by_locator(RegistrationLocators.hobby_dance).click()
        if 'reading' in hobby:
            self.get_element_by_locator(RegistrationLocators.hobby_reading).click()
        if 'cricket' in hobby:
            self.get_element_by_locator(RegistrationLocators.hobby_cricket).click()

    def select_list_value(self, list_locator: tuple[str, str], value: str):
        select = Select(self.get_element_by_locator(list_locator))
        select.select_by_value(value)

    def fill_out_form(self, data):
        with allure.step('Fill in "First Name" field'):
            self.fill_in_field(RegistrationLocators.first_name, data.first_name)
        with allure.step('Fill in "Last Name" field'):
            self.fill_in_field(RegistrationLocators.last_name, data.last_name)
        with allure.step('Select "Marital Status"'):
            self.select_marital_status(data.marital_status)
        with allure.step('Select "Hobby"'):
            if data.hobby:
                self.select_hobby(data.hobby)
        with allure.step('Select "Country" from drop down list'):
            self.select_list_value(RegistrationLocators.country, 'India')
        with allure.step('Select "Month" of "Date of Birth" from drop down list'):
            self.select_list_value(RegistrationLocators.date_of_birth_month, '1')
        with allure.step('Select "Day" of "Date of Birth" from drop down list'):
            self.select_list_value(RegistrationLocators.date_of_birth_day, '1')
        with allure.step('Select "Year" of "Date of Birth" from drop down list'):
            self.select_list_value(RegistrationLocators.date_of_birth_year, '2014')
        with allure.step('Fill in "Phone Number" field'):
            self.fill_in_field(RegistrationLocators.phone, data.phone)
        with allure.step('Fill in "Username" field'):
            self.fill_in_field(RegistrationLocators.username, environ['REG_FORM_USERNAME'])
        with allure.step('Fill in "E-mail" field'):
            self.fill_in_field(RegistrationLocators.email, data.email)
        with allure.step('Choose "Your Profile Picture"'):
            picture_path = os_path_join(Path(__file__).resolve().parents[1], 'tests', 'picture', 'ebersteiger.jpg')
            self.get_element_by_locator(RegistrationLocators.picture).send_keys(picture_path)
        with allure.step('Fill in "About Yourself" field'):
            self.fill_in_field(RegistrationLocators.about, data.about)
        with allure.step('Fill in "Password" field'):
            self.fill_in_field(RegistrationLocators.password, environ['REG_FORM_PASSWORD'])
        with allure.step('Fill in "Confirm Password" field'):
            self.fill_in_field(RegistrationLocators.confirm_password, environ['REG_FORM_PASSWORD'])

    def take_screenshot(self):
        with allure.step('Take a screenshot'):
            body = self.get_element_by_locator((By.TAG_NAME, 'body'))
            body.send_keys(Keys.PAGE_DOWN)
            allure.attach(self.browser.get_screenshot_as_png(),
                          name="Registration form filled",
                          attachment_type=AttachmentType.PNG)

    def submit_data(self):
        with allure.step('Submit data'):
            self.get_element_by_locator(RegistrationLocators.submit_button).submit()

    def assert_page_reloaded(self):
        with allure.step('Page reloaded'):
            assert self.get_current_url() == self.registration_page
            self.wait_for_visibility(RegistrationLocators.form)

    def find_not_existing_element(self):
        with allure.step('Try to find element by invalid locator'):
            invalid_locator = (By.ID, 'element not found')
            self.get_element_by_locator(invalid_locator)

