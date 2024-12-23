import allure
from allure import severity_level
from pytest import fixture

from pages import Homepage, Header, Certification, PopularCourses


@allure.severity(severity_level.BLOCKER)
@allure.epic("Smoke тест")
@allure.feature("Загрузка страницы")
@allure.testcase("Задачи U1, U2")
@allure.story("Страница загружается успешно, основные элементы отображаются корректно")
@allure.title("Загрузка главной страницы")
@allure.description(
    """
    Цель: Проверка открытия страницы

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Проверить значение "TITLE"
        3. Проверить корректность отображения элементов страницы

    Ожидаемый результат:
        - Значение "TITLE" соответствует главной странице
        - Элементы, уникальные для этой страницы, активны""")
def test_homepage(browser: fixture):
    homepage = Homepage(browser)
    homepage.open_homepage()
    homepage.check_page_title("Get Online Selenium Certification Course | Way2Automation")
    homepage.main_elements_are_active()


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Загрузка элемента страницы")
@allure.testcase("Задачи U1, U2")
@allure.story("Элемент загружается успешно")
@allure.title("Загрузка Header")
@allure.description(
    """
    Цель: Проверка данных в Header

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Проверить корректность отображения контактов
        3. Проверить корректность контактных данных

    Ожидаемый результат:
        - Номера телефонов и ссылки для связи кликабельны
        - Контактные номера и ссылки для связи корректны""")
def test_header(browser: fixture):
    header = Header(browser)
    header.open_homepage()
    header.contact_links_are_clickable()
    header.contact_data_is_valid()


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("Загрузка элемента страницы")
@allure.testcase("Задачи U1, U2")
@allure.story("Элемент загружается успешно")
@allure.title("Загрузка блока с сертификацией")
@allure.description(
    """
    Цель: Проверка блока с сертификацией

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Проверить заголовки элементов блока
        3. Проверить ссылки "Read More" элементов блока

    Ожидаемый результат:
        - Заголовок каждого элемента блока корректен
        - Ссылка кнопки "Read More" каждого блока корректна""")
def test_certification_block(browser: fixture):
    certification = Certification(browser)
    certification.open_homepage()
    certification.check_headers_of_block_elements()
    certification.check_links_of_block_elements()


@allure.severity(severity_level.MINOR)
@allure.epic("Smoke тест")
@allure.feature("Загрузка элемента страницы")
@allure.testcase("Задачи U1, U2")
@allure.story("Элемент загружается успешно")
@allure.title("Загрузка блока с курсами")
@allure.description(
    """
    Цель: Проверка блока с курсами

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть домашнюю страницу
        2. Прокрутить страницу до слайдов
        3. Нажать кнопку навигации "Назад"
        4. Проверить, что положение слайда изменилось
        5. Нажать кнопку навигации "Вперед"
        6. Проверить, что положение слайда изменилось

    Ожидаемый результат:
        - Положение слайда изменилось после нажатия кнопок навигации""")
def test_popular_courses_slider(browser: fixture):
    slider = PopularCourses(browser)
    slider.open_homepage()
    slider.scroll_to_slider()
    ini_location = slider.get_slide_location()
    slider.click_previous_button()
    slider.check_location_changed(ini_location)
    ini_location = slider.get_slide_location()
    slider.click_next_button()
    slider.check_location_changed(ini_location)
