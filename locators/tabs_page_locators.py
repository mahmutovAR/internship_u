from selenium.webdriver.common.by import By


class TabsLocators:
    link = (By.XPATH, '//a[string()="New Browser Tab"]')
    iframe = (By.TAG_NAME, 'iframe')
