import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then

from pages import Homepage, Header, Certification, PopularCourses


scenarios('./features/home_page.feature')


@pytest.fixture
def homepage(browser: fixture):
    return Homepage(browser)


@given('Homepage')
def homepage_open_page(homepage: fixture):
    homepage.open_homepage()


@then('Title is "Get Online Selenium Certification Course | Way2Automation"')
def homepage_check_title(homepage: fixture):
    homepage.check_page_title("Get Online Selenium Certification Course | Way2Automation")


@then('the main page elements are active')
def homepage_check_elements(homepage: fixture):
    homepage.main_elements_are_active()


@pytest.fixture
def header(browser: fixture):
    return Header(browser)


@then('Header link are clickable')
def header_check_links(header: fixture):
    header.contact_links_are_clickable()


@then('data is correct')
def homepage_check_data(header: fixture):
    header.contact_data_is_valid()


@pytest.fixture
def certification(browser: fixture):
    return Certification(browser)


@then('Certification Block link are clickable,')
def certification_check_elements(certification: fixture):
    certification.check_headers_of_block_elements()


@then('data is correct')
def certification_check_links(certification: fixture):
    certification.check_links_of_block_elements()


@pytest.fixture
def slider(browser: fixture):
    return PopularCourses(browser)


@when('Scroll to Courses Block')
def slider_scroll_to_block(slider: fixture):
    slider.scroll_to_slider()


@then('Courses Block navigation buttons are active')
def slider_check_nav_buttons(slider: fixture):
    ini_location = slider.get_slide_location()
    slider.click_previous_button()
    slider.check_location_changed(ini_location)
    ini_location = slider.get_slide_location()
    slider.click_next_button()
    slider.check_location_changed(ini_location)
