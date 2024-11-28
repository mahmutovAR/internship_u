from selenium.webdriver.common.by import By


class AuthCookiesLocators:
    login = (By.XPATH, '//input[@name="login"]')
    password = (By.XPATH, '//input[@name="psw"]')
    enter_button = (By.XPATH, '//input[@type="submit"]')
