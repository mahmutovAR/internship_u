import allure
from allure import severity_level
from pytest import fixture

from data import HeaderData
from pages import Homepage, Header, Certification, PopularCourses


@allure.severity(severity_level.BLOCKER)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка открытия страницы")
@allure.description(
    """
    Цель: Проверка открытия страницы

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть домашнюю страницу

    Ожидаемый результат:
        - Значение "TITLE" соответствует домашней странице
        - Элементы, уникальные для этой страницы, активны""")
def test_homepage(browser: fixture):
    homepage = Homepage(browser)
    homepage.open_homepage()
    title = homepage.get_page_title()
    expected_title = "Get Online Selenium Certification Course | Way2Automation"
    assert title == expected_title, f'Expected "{expected_title}" title, but got "{title}"'
    homepage.main_elements_are_active()


@allure.severity(severity_level.NORMAL)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка Header")
@allure.description(
    """
    Цель: Проверка данных в Header

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть домашнюю страницу

    Ожидаемый результат:
        - Номера телефонов и ссылки для связи кликабельны
        - Контактные номера и ссылки для связи корректны""")
def test_header(browser: fixture):
    header = Header(browser)
    header.open_homepage()
    header.contact_links__are_clickable()
    phone_1 = header.get_phone_number_1()
    phone_2 = header.get_phone_number_2()
    phone_3 = header.get_phone_number_3()
    skype = header.get_skype()
    email = header.get_email()
    assert phone_1 == HeaderData.phone_1, f'Expected "{HeaderData.phone_1}" data, but got {phone_1}'
    assert phone_2 == HeaderData.phone_2, f'Expected "{HeaderData.phone_2}" data, but got {phone_2}'
    assert phone_3 == HeaderData.phone_3, f'Expected "{HeaderData.phone_3}" data, but got {phone_3}'
    assert skype == HeaderData.skype, f'Expected "{HeaderData.skype}" data, but got {skype}'
    assert email == HeaderData.email, f'Expected "{HeaderData.email}" data, but got {email}'


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка блока с сертификацией")
@allure.description(
    """
    Цель: Проверка блока с сертификацией

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть домашнюю страницу

    Ожидаемый результат:
        - Заголовок каждого блока корректен
        - Ссылка кнопки "Read More" каждого блока корректна""")
def test_certification_block(browser: fixture):
    """Checks Certification block.
    1.4 Блок с сертификацией (Best Selenium Certification Course Online)
    - Блок с сертификацией присутствует и отображается корректно."""
    certification = Certification(browser)
    certification.open_homepage()
    certification.check_lifetime_membership()
    certification.check_online_training()
    certification.check_video_tutorials()
    certification.check_corporate_training()


@allure.severity(severity_level.MINOR)
@allure.epic("Тестирование www.way2automation.com")
@allure.feature("Homepage")
@allure.testcase(None, "Задача U1")
@allure.story("UI")
@allure.title("Проверка блока с курсами")
@allure.description(
    """
    Цель: Проверка блока с курсами

    Предусловие:
        - Открыть браузер

    Шаги:
         1. Открыть домашнюю страницу
         2. Прокрутить страницу до слайдов
         3. Нажать кнопку навигации "Назад"
         4. Нажать кнопку навигации "Вперед"

    Ожидаемый результат:
        - Положение слайда изменилось после нажатия кнопок навигации""")
def test_popular_courses_slider(browser: fixture):
    slider = PopularCourses(browser)
    slider.open_homepage()
    slider.scroll_to_slider()
    ini_location = slider.get_slide_location()
    slider.click_previous_button()
    location = slider.get_slide_location()
    assert ini_location != location, 'The slider was expected to move, but the location did not change'
    ini_location = slider.get_slide_location()
    slider.click_next_button()
    location = slider.get_slide_location()
    assert ini_location != location, 'The slider was expected to move, but the location did not change'
