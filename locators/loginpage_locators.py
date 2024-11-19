from selenium.webdriver.common.by import By


class LoginLocators:
    form = (By.XPATH, '//form[@name="form"]')
    username = (By.ID, "username")
    password = (By.ID, "password")
    username_desc = (By.ID, "formly_1_input_username_0")
    username_desc_2 = (By.ID, "formly_2_input_username_0")

    username_err = (By.XPATH, '//div[contains(@ng-class, "form.username") and contains(@class, "has-error")]')
    password_err = (By.XPATH, '//div[contains(@ng-class, "form.password") and contains(@class, "has-error")]')
    username_desc_err = (By.XPATH, '//div[contains(@class, "form-group ng-scope has-error")]')

    login_button = (By.XPATH, "//button[@ng-click='Auth.login()']")
    logout_link = (By.XPATH, '//a[@href="#/login"]')
    auth_success = (By.XPATH, """//div[contains(string(), "You're logged in!!")]""")
    auth_error = (By.XPATH, '//div[contains(@class, "alert alert-danger")]')

