from selenium.webdriver.common.by import By


class LoginLocators:
    username = (By.XPATH, '//input[@id="username"]')
    password = (By.XPATH, '//input[@id="password"]')
    username_desc = (By.XPATH, '//input[@id="formly_1_input_username_0"]')
    username_desc_2 = (By.XPATH, '//input[@id="formly_2_input_username_0"]')

    username_err = (By.XPATH, '//div[@ng-messages="form.username.$error"]/./div')
    password_err = (By.XPATH, '//div[@ng-messages="form.password.$error"]/./div')
    username_desc_err = (By.ID, 'formly_1_input_username_0_description')

    login_button = (By.XPATH, "//button[@ng-click='Auth.login()']")
    logout_link = (By.XPATH, '//a[contains(string(), "Logout")]')

    auth_success = (By.XPATH, """//p[contains(string(), "You're logged in!!")]""")
    auth_error = (By.XPATH, '//div[contains(@class, "alert alert-danger")]')
