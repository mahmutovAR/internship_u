from selenium.webdriver.common.by import By


class AuthCookiesLocators:
    login = (By.XPATH, '//input[@name="login"]')
    password = (By.XPATH, '//input[@name="psw"]')
    enter_button = (By.XPATH, '//input[@type="submit"]')
    login_guest = (By.XPATH, '//input[@value="user"]')
    password_guest = (By.XPATH, '//input[@value="dstu"]')
    enter_without_login = (By.XPATH, '//input[@type="submit" and @name="subm2"]')
    guest_auth = (By.XPATH, '//td[@align="right"]')
    logout_button = (By.XPATH, '//a[@href="/logout.php"]')


class AltAuthCookiesLocators:
    username = (By.ID, "username")
    password = (By.ID, "password")
    login = (By.XPATH, '//button[@type="submit"]')
    auth_message = (By.XPATH, '//div[contains(h2, "Secure Area")]')
    logout = (By.XPATH, '//a[@href="/logout"]')
