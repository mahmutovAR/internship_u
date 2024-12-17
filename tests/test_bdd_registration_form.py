from os.path import abspath, dirname
from os.path import join as os_path_join

import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then, parsers

from pages import RegistrationPage


scenarios('./features/registration_form.feature')


@pytest.fixture
def reg_form(browser: fixture):
    return RegistrationPage(browser)


@given('Registration Form page')
def open_page(reg_form: fixture):
    reg_form.open_form_page()
    

@when(parsers.parse('Fill first name: {first_name}'))
def fill_in_form_field(reg_form: fixture, first_name: str):
    reg_form.fill_first_name(first_name)


@when(parsers.parse('Fill last name: {last_name}'))
def fill_in_form_field(reg_form: fixture, last_name: str):
    reg_form.fill_last_name(last_name)


@when(parsers.parse('Select marital status: {marital_status}'))
def fill_in_form_field(reg_form: fixture, marital_status: str):
    reg_form.select_marital_status(marital_status)


@when(parsers.parse('Select hobby: {hobby}'))
def fill_in_form_field(reg_form: fixture, hobby: str):
    reg_form.select_hobby(hobby.split(','))


@when(parsers.parse('Select country: {country}'))
def fill_in_form_field(reg_form: fixture, country: str):
    reg_form.select_country(country)


@when(parsers.parse('Select birth month: {date_of_birth_month}'))
def fill_in_form_field(reg_form: fixture, date_of_birth_month: str):
    reg_form.select_birth_month(date_of_birth_month)


@when(parsers.parse('Select birth day: {date_of_birth_day}'))
def fill_in_form_field(reg_form: fixture, date_of_birth_day: str):
    reg_form.select_birth_day(date_of_birth_day)


@when(parsers.parse('Select birth year: {date_of_birth_year}'))
def fill_in_form_field(reg_form: fixture, date_of_birth_year: str):
    reg_form.select_birth_year(date_of_birth_year)


@when(parsers.parse('Fill phone: {phone}'))
def fill_in_form_field(reg_form: fixture, phone: str):
    reg_form.fill_phone(phone)


@when(parsers.parse('Fill username: {username}'))
def fill_in_form_field(reg_form: fixture, username: str):
    reg_form.fill_username(username)


@when(parsers.parse('Fill email: {email}'))
def fill_in_form_field(reg_form: fixture, email: str):
    reg_form.fill_email(email)


@when(parsers.parse('Choose picture: {picture_name}'))
def fill_in_form_field(reg_form: fixture, picture_name: str):
    reg_form.choose_picture(os_path_join(dirname(abspath(__file__)), 'picture', picture_name))


@when(parsers.parse('Fill about: {about}'))
def fill_in_form_field(reg_form: fixture, about: str):
    reg_form.fill_about(about)


@when(parsers.parse('Fill password: {password}'))
def fill_in_form_field(reg_form: fixture, password: str):
    reg_form.fill_password(password)


@when(parsers.parse('Confirm password: {confirm_password}'))
def fill_in_form_field(reg_form: fixture, confirm_password: str):
    reg_form.fill_confirm_password(confirm_password)


@when('Submit data')
def fill_in_form_field(reg_form: fixture):
    reg_form.submit_data()


@then('No error found')
def fill_in_form_field(reg_form: fixture):
    reg_form.no_error_found()
