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
        self.element_is_present(MainElementsLocators.header)
        self.element_is_present(MainElementsLocators.block_1)
        self.element_is_present(MainElementsLocators.block_2)
        self.element_is_present(MainElementsLocators.block_3)
        self.element_is_present(MainElementsLocators.live_trainings)
        self.element_is_present(MainElementsLocators.footer)


class Header(BasePage):
    def data_is_valid(self, locator: tuple[str, str], data: str) -> None:
        self.element_is_present(locator)
        assert self.browser.find_element(*locator).text == data

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
        self.go_to_homepage()
        self.close_ads()
        self.click_element(locator)
        assert self.browser.current_url == data

    def click_menu_items(self) -> None:
        self.assert_redirect(MenuLocators.home, MenuLinksData.home)
        self.assert_redirect(MenuLocators.all_courses, MenuLinksData.all_courses)
        self.assert_redirect(MenuLocators.video_tutorial, MenuLinksData.video_tutorial)
        self.assert_redirect(MenuLocators.resources, MenuLinksData.resources)
        self.assert_redirect(MenuLocators.careers, MenuLinksData.careers)
        self.assert_redirect(MenuLocators.lifetime_membership, MenuLinksData.lifetime_membership)
        self.assert_redirect(MenuLocators.blog, MenuLinksData.blog)
        self.assert_redirect(MenuLocators.forum, MenuLinksData.forum)
        self.assert_redirect(MenuLocators.member_login, MenuLinksData.member_login)

    def element_is_clickable_when_scrolling(self, locator: tuple[str, str]) -> None:
        self.go_to_homepage()
        self.browser.execute_script('window.scrollBy(0, 3500);')
        self.close_ads()
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator))

    def menu_items_are_clickable_when_scrolling(self) -> None:
        self.element_is_clickable_when_scrolling(MenuLocators.home)
        self.element_is_clickable_when_scrolling(MenuLocators.all_courses)
        self.element_is_clickable_when_scrolling(MenuLocators.video_tutorial)
        self.element_is_clickable_when_scrolling(MenuLocators.resources)
        self.element_is_clickable_when_scrolling(MenuLocators.careers)
        self.element_is_clickable_when_scrolling(MenuLocators.lifetime_membership)
        self.element_is_clickable_when_scrolling(MenuLocators.blog)
        self.element_is_clickable_when_scrolling(MenuLocators.forum)
        self.element_is_clickable_when_scrolling(MenuLocators.member_login)

    def hover_over_element(self, locator: tuple[str, str]):
        actions = ActionChains(self.browser)
        element = self.browser.find_element(*locator)
        actions.move_to_element(element).perform()

    def check_link_all_courses_appium_python(self) -> None:
        self.go_to_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.all_courses)
        self.hover_over_element(MenuRedirectLocators.all_courses_appium)
        self.click_element(MenuRedirectLocators.all_courses_appium_python)
        assert self.browser.current_url == MenuRedirectData.all_courses_appium_python
        self.page_loaded()

    def check_link_video_tutorial_spring(self) -> None:
        self.go_to_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.video_tutorial)
        self.click_element(MenuRedirectLocators.video_tutorial_spring)
        assert self.browser.current_url == MenuRedirectData.video_tutorial_spring
        self.page_loaded()

    def check_resources_site_1(self) -> None:
        self.go_to_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.resources)
        self.click_element(MenuRedirectLocators.resources_site_1)
        assert self.browser.current_url == MenuRedirectData.resources_site_1
        self.page_loaded()

    def check_resources_blog(self) -> None:
        self.go_to_homepage()
        self.close_ads()
        self.hover_over_element(MenuLocators.resources)
        self.click_element(MenuRedirectLocators.resources_blog)
        assert self.browser.current_url == MenuRedirectData.resources_blog
        self.page_loaded()


class Certification(BasePage):
    def check_block(self) -> None:
        self.element_is_present(CertificationLocators.lifetime_membership)
        self.element_is_present(CertificationLocators.online_training)
        self.element_is_present(CertificationLocators.video_tutorials)
        self.element_is_present(CertificationLocators.corporate_training)


class PopularCourses(BasePage):
    def check_navigation_button(self, locator: tuple[str, str]):
        self.close_ads()
        js_scroll_code = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js_scroll_code, self.browser.find_element(*PopularCoursesLocators.main))

        button = self.browser.find_element(*locator)
        slide = self.browser.find_element(*PopularCoursesLocators.slide)
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
        self.element_is_present(FooterLocators.main)
        self.element_is_present(FooterLocators.about_us)
        self.element_is_present(FooterLocators.address)
        self.element_is_present(FooterLocators.phone_1)
        self.element_is_present(FooterLocators.phone_2)
        self.element_is_present(FooterLocators.email_1)
        self.element_is_present(FooterLocators.email_2)
        self.element_is_present(FooterLocators.info)
