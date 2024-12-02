from selenium.webdriver.common.by import By


class AlertsLocators:
    input_alert = (By.XPATH, '//a[string()="Input Alert"]')
    iframe = (By.XPATH, '//iframe[@src="alert/input-alert.html"]')
    input_box = (By.XPATH, '//button[contains(string(), "Input box")]')
    message = (By.XPATH, "/html/body/p")
