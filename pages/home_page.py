from time import sleep

import allure
from selenium.webdriver.common.by import By

from data import HeaderData, PageUrls, MenuUrls
from locators import (UniqueElementsLocators, HeaderLocators, MenuLocators,
                      CertificationLocators, PopularCoursesLocators,
                      MenuRedirectLocators)
from . import BasePage


class Homepage(BasePage):
    def open_homepage(self) -> None:
        with allure.step('Открыть домашнюю страницу'):
            self.open_url(PageUrls.homepage)

    def check_link_to_be_clickable(self, locator: tuple[str, str]) -> None:
        link = self.get_clickable_element(locator)
        assert link, f'Expected "{link}" to be clickable'

    def check_page_title(self, expected_title: str) -> None:
        with allure.step('Проверить значение "TITLE"'):
            title = self.get_page_title()
            assert title == expected_title, f'Expected "{expected_title}" title, but got "{title}"'

    def main_elements_are_active(self) -> None:
        with allure.step('Проверить корректность отображения элементов страницы'):
            self.check_link_to_be_clickable(UniqueElementsLocators.link_about_us)
            self.check_link_to_be_clickable(UniqueElementsLocators.link_view_all_images)


class Header(Homepage):
    def contact_links_are_clickable(self) -> None:
        with allure.step('Проверить корректность отображения контактов'):
            for locator in HeaderLocators.all_items:
                self.check_link_to_be_clickable(locator)

    def contact_data_is_valid(self) -> None:
        with allure.step('Проверить корректность контактных данных'):
            for contact_locator, expected_data in zip(HeaderLocators.contacts, HeaderData.all_items):
                data = self.get_element_text(contact_locator)
                assert data == expected_data, f'Expected "{expected_data}" data, but got "{data}"'


class Menu(Homepage):
    def scroll_to_footer(self) -> None:
        with allure.step('Прокрутить страницу до блока "Footer"'):
            self.scroll_to_element(MenuLocators.footer)

    def menu_items_are_visible_and_clickable(self) -> None:
        with allure.step('Проверить, что основные пункты меню отображаются и кликабельны'):
            for locator in MenuLocators.all_items:
                assert self.element_is_visible(locator), 'Menu items expected to be visible'
                assert self.get_clickable_element(locator), 'Menu items expected to be clickable'

    def hover_over_all_courses(self) -> None:
        with allure.step('Навести курсор на вкладку меню "All Courses"'):
            self.hover_over_element(MenuLocators.all_courses)

    def click_appium(self) -> None:
        with allure.step('Кликнуть пункт "Appium"'):
            self.click_element(MenuRedirectLocators.all_courses_appium)

    def click_appium_python(self) -> None:
        with allure.step('Кликнуть пункт "Appium with Python"'):
            self.click_element(MenuRedirectLocators.all_courses_appium_python)

    def assert_redirection_to_appium_python(self) -> None:
        with allure.step('Проверить переход на страницу'):
            curr_url = self.get_current_url()
            expected_url = MenuUrls.appium_python
            assert curr_url == expected_url, f'Expected redirection to "{expected_url}", but got "{curr_url}"'

    def appium_python_elements_are_active(self) -> None:
        with allure.step('Проверить корректность отображения элементов страницы'):
            link_1 = self.get_clickable_element(MenuRedirectLocators.appium_python_link_1)
            link_2 = self.get_clickable_element(MenuRedirectLocators.appium_python_link_2)
            assert link_1, f'Expected "{link_1}" to be clickable'
            assert link_2, f'Expected "{link_2}" to be clickable'

    def hover_over_video_tutorial(self) -> None:
        with allure.step('Навести курсор на вкладку меню "Video Tutorial"'):
            self.hover_over_element(MenuLocators.video_tutorial)

    def click_spring_boot(self) -> None:
        with allure.step('Кликнуть пункт "Spring Boot"'):
            self.click_element(MenuRedirectLocators.video_tutorial_spring)

    def assert_redirection_to_spring_boot(self) -> None:
        with allure.step('Проверить переход на страницу'):
            curr_url = self.get_current_url()
            expected_url = MenuUrls.spring_boot
            assert curr_url == expected_url, f'Expected redirection to "{expected_url}", but got "{curr_url}"'

    def spring_boot_elements_are_active(self) -> None:
        with allure.step('Проверить корректность отображения элементов страницы'):
            link_1 = self.get_clickable_element(MenuRedirectLocators.spring_boot_link)
            element_1_text = self.get_element_text(MenuRedirectLocators.spring_boot_text_1)
            element_2_text = self.get_element_text(MenuRedirectLocators.spring_boot_text_2)
            expected_text_1 = 'When does the course start and finish?'
            expected_text_2 = 'Get started now!'
            assert link_1, f'Expected {link_1} to be clickable'
            assert element_1_text == expected_text_1, f'Expected text "{expected_text_1}" is present, but got "{element_1_text}"'
            assert element_2_text == expected_text_2, f'Expected text "{expected_text_2}" is present, but got "{element_2_text}"'


class Certification(Homepage):
    def check_header(self, heading_locator: tuple[str, str], expected_text: str) -> None:
        heading = self.get_nested_element_text(heading_locator, (By.TAG_NAME, 'h3'))
        assert heading == expected_text, f'Expected text "{expected_text}", but got "{heading}"'

    def check_link(self, link_locator: tuple[str, str], expected_link: str) -> None:
        link = self.get_nested_element_link(link_locator, (By.TAG_NAME, 'a'))
        assert link == expected_link, f'Expected text "{expected_link}", but got "{link}"'

    def check_headers_of_block_elements(self) -> None:
        with allure.step('Проверить заголовки элементов блока'):
            self.check_header(CertificationLocators.lifetime_membership,
                              'Lifetime Membership')

            self.check_header(CertificationLocators.online_training,
                              'Online Training')

            self.check_header(CertificationLocators.video_tutorials,
                              """Video Tutorials
(Best Selenium Tutorial)""")

            self.check_header(CertificationLocators.corporate_training,
                              'Corporate Training')

    def check_links_of_block_elements(self) -> None:
        with allure.step('Проверить ссылки "Read More" элементов блока'):
            self.check_link(CertificationLocators.lifetime_membership_button,
                            MenuUrls.lifetime_membership)

            self.check_link(CertificationLocators.online_training_button,
                            MenuUrls.online_training)

            self.check_link(CertificationLocators.video_tutorials_button,
                            MenuUrls.video_tutorials)

            self.check_link(CertificationLocators.corporate_training_button,
                            MenuUrls.corporate_training)


class PopularCourses(Homepage):
    def scroll_to_slider(self) -> None:
        with allure.step('Прокрутить страницу до слайдов'):
            self.scroll_to_element(PopularCoursesLocators.prev_slide)

    def get_slide_location(self) -> dict:
        return self.get_element_by_locator(PopularCoursesLocators.slide).location

    def click_previous_button(self) -> None:
        with allure.step('Нажать кнопку навигации "Назад"'):
            self.click_element(PopularCoursesLocators.prev_slide)
            sleep(0.5)

    def check_location_changed(self, prev_position: dict):
        with allure.step('Проверить, что положение слайда изменилось'):
            assert prev_position != self.get_slide_location(), 'The slider was expected to move, but the location did not change'

    def click_next_button(self) -> None:
        with allure.step('Нажать кнопку навигации "Вперед"'):
            self.click_element(PopularCoursesLocators.next_slide)
            sleep(0.5)
