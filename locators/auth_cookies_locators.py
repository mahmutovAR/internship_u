from selenium.webdriver.common.by import By


class AuthCookiesLocators:
    login = (By.XPATH, '//input[@name="login"]')
    password = (By.XPATH, '//input[@name="psw"]')
    enter_button = (By.XPATH, '//input[@type="submit"]')
    enter_without_login = (By.XPATH, '//input[@type="submit" and @name="subm2"]')
    guest_auth = (By.XPATH, '//td[@align="right"]')
    logout_button = (By.XPATH, '//a[@href="/logout.php"]')
