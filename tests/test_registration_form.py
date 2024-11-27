from os.path import abspath, dirname
from os.path import join as os_path_join
from random import choice, randrange, sample

import allure
import pytest
from allure import severity_level
from pytest import fixture

from pages import RegistrationPage


@allure.severity(severity_level.CRITICAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Registration Form")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Заполнение формы")
@allure.description(
    """
    Цель: Проверить заполнение формы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу с формой
        2. Заполнить поле "First Name"
        3. Заполнить поле "Last Name"
        4. Выбрать "Marital Status"
        5. Выбрать "Hobby"
        6. Выбрать "Country" из выпадающего списка
        7. Выбрать "Month" поля "Date of Birth" из выпадающего списка
        8. Выбрать "Day" поля "Date of Birth" из выпадающего списка
        9. Выбрать "Year" поля "Date of Birth" из выпадающего списка
        10. Заполнить поле "Phone Number"
        11. Заполнить поле "Username"
        12. Заполнить поле "E-mail"
        13. Загрузить изображение в поле "Your Profile Picture"
        14. Заполнить поле "About Yourself"
        15. Заполнить поле "Password"
        16. Заполнить поле "Confirm Password"
        18. Нажать на кнопку "SUBMIT"

    Ожидаемый результат:
        - Нет сообщений о некорректном вводе данных""")
@pytest.mark.parametrize('registration_form_data',
                         [{'marital_status': choice(['single', 'married', 'divorced']),
                           'hobby': sample(['dance', 'reading', 'cricket'], k=randrange(1, 3)),
                           'country': 'India',
                           'date_of_birth_month': 1,
                           'date_of_birth_day': 1,
                           'date_of_birth_year': 2014,
                           'picture_path': os_path_join(dirname(abspath(__file__)), 'picture', 'ebersteiger.jpg')}],
                         indirect=True)
def test_fill_out_form(browser: fixture, registration_form_data: fixture):
    login_page = RegistrationPage(browser)
    login_page.open_form_page()
    form_data = registration_form_data
    login_page.fill_first_name(form_data.first_name)
    login_page.fill_last_name(form_data.last_name)
    login_page.select_marital_status(form_data.marital_status)
    login_page.select_hobby(form_data.hobby)
    login_page.select_country(form_data.country)
    login_page.select_birth_month(form_data.date_of_birth_month)
    login_page.select_birth_day(form_data.date_of_birth_day)
    login_page.select_birth_year(form_data.date_of_birth_year)
    login_page.fill_phone(form_data.phone)
    login_page.fill_username(form_data.username)
    login_page.fill_email(form_data.email)
    if form_data.picture_path:
        login_page.choose_picture(form_data.picture_path)
    login_page.fill_about(form_data.about)
    login_page.fill_password(form_data.password)
    login_page.fill_confirm_password(form_data.confirm_password)
    login_page.submit_data()
    login_page.no_error_found()
