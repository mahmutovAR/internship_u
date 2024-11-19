from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import LoginLocators
from . import BasePage


class LoginPage(BasePage):
    def go_to_login(self):
        self.browser.get('https://www.way2automation.com/angularjs-protractor/registeration/#/login')
        self.wait_for_visibility(LoginLocators.form)

    def check_fields(self):
        self.element_is_present(LoginLocators.username)
        self.element_is_present(LoginLocators.password)
        self.element_is_present(LoginLocators.username_desc)

    def check_empty_form(self):
        body = self.browser.find_element(By.TAG_NAME, 'body')
        for _ in range(4):
            body.send_keys(Keys.TAB)
        self.element_is_present(LoginLocators.username_err)
        self.element_is_present(LoginLocators.password_err)
        self.element_is_present(LoginLocators.username_desc_err)

    def log_in_valid(self, username: str, password: str, username_desc: str):
        self.browser.find_element(*LoginLocators.username).send_keys(username)
        self.browser.find_element(*LoginLocators.password).send_keys(password)
        self.browser.find_element(*LoginLocators.username_desc).send_keys(username_desc)
        self.browser.find_element(*LoginLocators.login_button).click()
        self.element_is_present(LoginLocators.auth_success)

    def log_in_invalid(self, username: str, password: str, username_desc: str):
        self.browser.find_element(*LoginLocators.username).send_keys(username)
        self.browser.find_element(*LoginLocators.password).send_keys(password)
        self.browser.find_element(*LoginLocators.username_desc).send_keys(username_desc)
        self.browser.find_element(*LoginLocators.login_button).click()
        self.element_is_present(LoginLocators.auth_error)

    def log_out(self):
        self.browser.find_element(*LoginLocators.logout_link).click()
        self.element_is_present(LoginLocators.username)
        self.element_is_present(LoginLocators.password)
        self.element_is_present(LoginLocators.username_desc_2)
