import allure
from allure import severity, severity_level
from pytest import fixture

from pages import RegistrationPage


@severity(severity_level.CRITICAL)
@allure.epic("UI testing")
@allure.feature("Registration Form")
@allure.story("Log in")
@allure.title("Fill out form with valid data")
@allure.description(
    """
    Task: Log out Registration Form

    SetUp:
        - open browser

    Steps:
         1. Open "Registration Form" url
         2. Fill in "First Name" field
         3. Fill in "Last Name" field
         4. Select "Marital Status"
         5. Select "Hobby"
         6. Select "Country" from drop down list
         7. Select "Month" of "Date of Birth" from drop down list
         8. Select "Day" of "Date of Birth" from drop down list
         9. Select "Year" of "Date of Birth" from drop down list
        10. Fill in "Phone Number" field
        11. Fill in "Username" field
        12. Fill in "E-mail" field
        13. Choose "Your Profile Picture"
        14. Fill in "About Yourself" field
        15. Fill in "Password" field
        16. Fill in "Confirm Password" field
        17. Take a screenshot 
        18. Submit data

    Expected result:
        - all fields filled before submitting
        - page reloaded after submitting""")
def test_fill_out_form(browser: fixture, form_data: fixture):
    """Fills the registration form with the generated data."""
    login_page = RegistrationPage(browser)
    login_page.go_to_form_page()
    login_page.fill_out_form(form_data)
    login_page.take_screenshot()
    login_page.submit_data()
    login_page.assert_page_reloaded()


@severity(severity_level.MINOR)
@allure.epic("UI testing")
@allure.feature("Registration Form")
@allure.story("Log in")
@allure.title("Test failure screenshot")
@allure.description(
    """
    Task: Log out Registration Form

    SetUp:
        - open browser

    Steps:
         1. Open "Registration Form" url
         2. Try to find element by invalid locator
         3. Take screenshot of test failure

    Expected result:
        - test failed, screenshot taken""")
def test_fill_out_form(browser: fixture, form_data: fixture):
    """Fills the registration form with the generated data."""
    login_page = RegistrationPage(browser)
    login_page.go_to_form_page()
    login_page.find_not_existing_element()
