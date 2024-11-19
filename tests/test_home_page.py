from pytest import fixture

from pages import (Homepage, Header, Menu, Certification,
                   PopularCourses, Footer)


def test_homepage(browser: fixture):
    """Checks that the home page loads and that basic elements are present."""
    homepage = Homepage(browser)
    homepage.go_to_homepage()
    homepage.page_loaded()
    homepage.main_elements_are_present()


def test_header(browser: fixture):
    """Checks header with contact information."""
    header = Header(browser)
    header.go_to_homepage()
    header.contact_information_is_present_and_actual()
    header.social_networks_are_present()


def test_menu(browser: fixture):
    """Checks that menu elements are present."""
    menu = Menu(browser)
    menu.go_to_homepage()
    menu.click_menu_items()


def test_certification_block(browser: fixture):
    """Checks Certification block."""
    certification = Certification(browser)
    certification.go_to_homepage()
    certification.check_block()


def test_popular_courses_slider(browser: fixture):
    """Checks navigation buttons."""
    slider = PopularCourses(browser)
    slider.go_to_homepage()
    slider.check_previous_course_button()
    slider.check_next_course_button()


def test_footer(browser: fixture):
    """Checks the footer for company information and contacts."""
    footer = Footer(browser)
    footer.go_to_homepage()
    footer.check_footer()
