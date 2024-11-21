from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from data import HeaderData, MenuLinksData, MenuRedirectData
from locators import (MainElementsLocators, HeaderLocators, MenuLocators,
                      CertificationLocators, PopularCoursesLocators,
                      FooterLocators, MenuRedirectLocators)
from . import BasePage


class Homepage(BasePage):
    def main_elements_are_present(self) -> None:
        self.last_page_element_loaded(self.ads_locator)
        for locator in MainElementsLocators.all_items:
            self.element_is_present(locator)


class Header(BasePage):
    def data_is_valid(self, locator: tuple[str, str], data: str) -> None:
        self.element_is_present(locator)
        assert self.get_element_by_locator(locator).text == data

    def contact_information_is_present_and_actual(self) -> None:
        self.data_is_valid(HeaderLocators.phone_number_1, HeaderData.phone_number_1)
        self.data_is_valid(HeaderLocators.phone_number_2, HeaderData.phone_number_2)
        self.data_is_valid(HeaderLocators.phone_number_3, HeaderData.phone_number_3)
        self.data_is_valid(HeaderLocators.skype, HeaderData.skype)
        self.data_is_valid(HeaderLocators.email, HeaderData.email)

    def social_networks_are_present(self) -> None:
        self.element_is_present(HeaderLocators.facebook)
        self.element_is_present(HeaderLocators.linkedin)
        self.element_is_present(HeaderLocators.plus_google)
        self.element_is_present(HeaderLocators.youtube)


class Menu(BasePage):
    def assert_redirect(self, locator: tuple[str, str], data: str) -> None:
        self.get_homepage()
        self.close_ads()
        self.click_element(locator)
        assert self.get_current_url() == data

    def click_menu_items(self) -> None:
        for locator, data in zip(MenuLocators.all_items, MenuLinksData.all_items):
            self.assert_redirect(locator, data)

    def element_is_clickable_when_scrolling(self, locator: tuple[str, str]) -> None:
        self.get_homepage()
        self.scroll_page()
        self.close_ads()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))

    def menu_items_are_clickable_when_scrolling(self) -> None:
        for locator in MenuLocators.all_items:
            self.element_is_clickable_when_scrolling(locator)

    def hover_over_element(self, locator: tuple[str, str]):
        actions = ActionChains(self.browser)
        element = self.get_element_by_locator(locator)
        actions.move_to_element(element).perform()

    def check_link_all_courses_appium_python(self) -> None:
        self.get_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.all_courses)
        self.hover_over_element(MenuRedirectLocators.all_courses_appium)
        self.click_element(MenuRedirectLocators.all_courses_appium_python)
        assert self.get_current_url() == MenuRedirectData.all_courses_appium_python
        self.last_page_element_loaded(self.ads_locator)

    def check_link_video_tutorial_spring(self) -> None:
        self.get_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.video_tutorial)
        self.click_element(MenuRedirectLocators.video_tutorial_spring)
        assert self.get_current_url() == MenuRedirectData.video_tutorial_spring
        self.last_page_element_loaded(MenuRedirectLocators.video_tutorial_spring_loaded)

    def check_resources_site_1(self) -> None:
        self.get_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.resources)
        self.click_element(MenuRedirectLocators.resources_site_1)
        assert self.get_current_url() == MenuRedirectData.resources_site_1
        self.last_page_element_loaded(MenuRedirectLocators.resources_site_1_loaded)

    def check_resources_blog(self) -> None:
        self.get_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.resources)
        self.click_element(MenuRedirectLocators.resources_blog)
        assert self.get_current_url() == MenuRedirectData.resources_blog
        self.last_page_element_loaded(MenuRedirectLocators.resources_blog_loaded)


class Certification(BasePage):
    def check_block(self) -> None:
        for locator in CertificationLocators.all_items:
            self.element_is_present(locator)


class PopularCourses(BasePage):
    def check_navigation_button(self, locator: tuple[str, str]):
        self.close_ads()
        self.scroll_to_element(PopularCoursesLocators.main)

        button = self.get_element_by_locator(locator)
        slide = self.get_element_by_locator(PopularCoursesLocators.slide)
        ini_location = slide.location
        button.click()
        sleep(0.5)
        prev_location = slide.location
        assert ini_location != prev_location

    def check_previous_course_button(self) -> None:
        self.check_navigation_button(PopularCoursesLocators.prev_slide)

    def check_next_course_button(self) -> None:
        self.check_navigation_button(PopularCoursesLocators.next_slide)


class Footer(BasePage):
    def check_footer(self):
        for locator in FooterLocators.all_items:
            self.element_is_present(locator)
