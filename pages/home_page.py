from time import sleep

import allure
from selenium.webdriver.common.by import By

from data import URL, MenuUrls
from locators import (UniqueElementsLocators, HeaderLocators, MenuLocators,
                      CertificationLocators, PopularCoursesLocators,
                      MenuRedirectLocators)
from . import BasePage


class Homepage(BasePage):
    def open_homepage(self) -> None:
        with allure.step('Открыть домашнюю страницу'):
            self.open_url(URL.homepage)

    def check_link_to_be_clickable(self, locator: tuple[str, str]) -> None:
        link = self.element_is_clickable(locator)
        assert link, f'Expected {link} to be clickable'

    def main_elements_are_active(self) -> None:
        self.check_link_to_be_clickable(UniqueElementsLocators.link_about_us)
        self.check_link_to_be_clickable(UniqueElementsLocators.link_view_all_images)


class Header(Homepage):
    def contact_links__are_clickable(self) -> None:
        for locator in HeaderLocators.all_items:
            self.check_link_to_be_clickable(locator)

    def get_phone_number_1(self) -> str:
        return self.get_element_text(HeaderLocators.phone_number_1)

    def get_phone_number_2(self) -> str:
        return self.get_element_text(HeaderLocators.phone_number_2)

    def get_phone_number_3(self) -> str:
        return self.get_element_text(HeaderLocators.phone_number_3)

    def get_skype(self) -> str:
        return self.get_element_text(HeaderLocators.skype)

    def get_email(self) -> str:
        return self.get_element_text(HeaderLocators.email)


class Menu(Homepage):
    def scroll_to_footer(self) -> None:
        with allure.step('Прокрутить страницу до блока "Footer"'):
            self.scroll_to_element(MenuLocators.footer)

    def menu_items_are_visible_and_clickable(self) -> None:
        for locator in MenuLocators.all_items:
            assert self.element_is_visible(locator), 'Menu items expected to be visible'
            assert self.element_is_clickable(locator), 'Menu items expected to be clickable'

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
        curr_url = self.get_current_url()
        expected_url = MenuUrls.appium_python
        assert curr_url == expected_url, f'Expected redirection to {expected_url}, but got {curr_url}'

    def appium_python_elements_are_active(self) -> None:
        link_1 = self.element_is_clickable(MenuRedirectLocators.appium_python_link_1)
        link_2 = self.element_is_clickable(MenuRedirectLocators.appium_python_link_2)
        assert link_1, f'Expected {link_1} to be clickable'
        assert link_2, f'Expected {link_2} to be clickable'

    def hover_over_video_tutorial(self) -> None:
        with allure.step('Навести курсор на вкладку меню "Video Tutorial"'):
            self.hover_over_element(MenuLocators.video_tutorial)

    def click_spring_boot(self) -> None:
        with allure.step('Кликнуть пункт "Spring Boot"'):
            self.click_element(MenuRedirectLocators.video_tutorial_spring)

    def assert_redirection_to_spring_boot(self) -> None:
        curr_url = self.get_current_url()
        expected_url = MenuUrls.spring_boot
        assert curr_url == expected_url, f'Expected redirection to {expected_url}, but got {curr_url}'

    def spring_boot_elements_are_active(self) -> None:
        link_1 = self.element_is_clickable(MenuRedirectLocators.spring_boot_link)
        element_1_text = self.get_element_text(MenuRedirectLocators.spring_boot_text_1)
        element_2_text = self.get_element_text(MenuRedirectLocators.spring_boot_text_2)
        expected_text_1 = 'When does the course start and finish?'
        expected_text_2 = 'Get started now!'
        assert link_1, f'Expected {link_1} to be clickable'
        assert element_1_text == expected_text_1, f'Expected text "{expected_text_1}" is present, but got "{element_1_text}"'
        assert element_2_text == expected_text_2, f'Expected text "{expected_text_2}" is present, but got "{element_2_text}"'


class Certification(Homepage):
    def check_block(self, heading_locator: tuple[str, str], link_locator: tuple[str, str],
                    expected_text: str, expected_link: str) -> None:
        heading = self.get_nested_element_text(heading_locator, (By.TAG_NAME, 'h3'))
        assert heading == expected_text, f'Expected text {expected_text}, but got {heading}'

        link = self.get_nested_element_link(link_locator, (By.TAG_NAME, 'a'))
        assert link == expected_link, f'Expected text {expected_link}, but got {link}'

    def check_lifetime_membership(self) -> None:
        self.check_block(CertificationLocators.lifetime_membership,
                         CertificationLocators.lifetime_membership_button,
                         'Lifetime Membership',
                         "https://www.way2automation.com/lifetime-membership-club/")

    def check_online_training(self) -> None:
        self.check_block(CertificationLocators.online_training,
                         CertificationLocators.online_training_button,
                         'Online Training',
                         "https://www.way2automation.com/selenium-training/online-training-webinars/")

    def check_video_tutorials(self) -> None:
        self.check_block(CertificationLocators.video_tutorials,
                         CertificationLocators.video_tutorials_button,
                         """Video Tutorials
(Best Selenium Tutorial)""",
                         "https://www.selenium-tutorial.com/courses/")

    def check_corporate_training(self) -> None:
        self.check_block(CertificationLocators.corporate_training,
                         CertificationLocators.corporate_training_button,
                         'Corporate Training',
                         "https://www.way2automation.com/#elementor-action%3Aaction%3Dpopup%3Aopen%26settings%3DeyJpZCI6IjI1NDY1IiwidG9nZ2xlIjpmYWxzZX0%3D")


class PopularCourses(Homepage):
    def scroll_to_slider(self) -> None:
        with allure.step('Прокрутить страницу до слайдов'):
            self.scroll_to_element(PopularCoursesLocators.main)

    def get_slide_location(self) -> dict:
        return self.get_element_by_locator(PopularCoursesLocators.slide).location

    def click_previous_button(self) -> None:
        with allure.step('Нажать кнопку навигации "Назад"'):
            self.click_element(PopularCoursesLocators.prev_slide)
            sleep(0.5)

    def click_next_button(self) -> None:
        with allure.step('Нажать кнопку навигации "Вперед"'):
            self.click_element(PopularCoursesLocators.next_slide)
            sleep(0.5)
