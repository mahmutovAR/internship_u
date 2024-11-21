from pytest import fixture

from pages import (Homepage, Header, Menu, Certification,
                   PopularCourses, Footer)


def test_homepage(browser: fixture):
    """Checks that the home page loads and that basic elements are present.
    1.1 Проверка открытия страницы
    - Страница загружается успешно.
    - Все основные элементы отображаются корректно."""
    homepage = Homepage(browser)
    homepage.get_homepage()
    homepage.main_elements_are_present()


def test_header(browser: fixture):
    """Checks header with contact information.
    1.2 Проверка хедера с контактной информацией
    - Хедер содержит номера телефонов и ссылки для связи, и они кликабельны.
    - Проверка отображения и корректности контактной информации:
    убедиться, что все контактные номера и ссылки для связи актуальны."""
    header = Header(browser)
    header.get_homepage()
    header.contact_information_is_present_and_actual()
    header.social_networks_are_present()


def test_menu(browser: fixture):
    """Checks that menu elements are present.
    1.3 Проверка выпадающих списков
    - Функциональность: при клике на каждый пункт меню происходит переход на соответствующую страницу."""
    menu = Menu(browser)
    menu.get_homepage()
    menu.click_menu_items()


def test_certification_block(browser: fixture):
    """Checks Certification block.
    1.4 Блок с сертификацией (Best Selenium Certification Course Online)
    - Блок с сертификацией присутствует и отображается корректно."""
    certification = Certification(browser)
    certification.get_homepage()
    certification.check_block()


def test_popular_courses_slider(browser: fixture):
    """Checks navigation buttons.
    1.5 Блок с курсами (Most Popular Software Testing Courses)
    Проверка кнопок навигации (вперед и назад): они работают корректно и меняют слайды."""
    slider = PopularCourses(browser)
    slider.get_homepage()
    slider.check_previous_course_button()
    slider.check_next_course_button()


def test_footer(browser: fixture):
    """Checks the footer for company information and contacts.
    1.6 Футер
    - Футер отображается корректно и содержит:
        - Ссылки на социальные сети.
        - Информацию о компании, контактные данные."""
    footer = Footer(browser)
    footer.get_homepage()
    footer.check_footer()
