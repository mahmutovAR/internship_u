from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.url = 'https://www.way2automation.com/'

    def go_to_homepage(self) -> None:
        self.browser.get(self.url)

    def close_ads(self) -> None:
        body = self.browser.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_UP)
        from time import sleep
        sleep(6)
        body.send_keys(Keys.ESCAPE)

        # body = self.browser.find_element(By.TAG_NAME, 'body')
        # body.send_keys(Keys.PAGE_DOWN)
        # body.send_keys(Keys.PAGE_UP)
        # ads = (By.XPATH, '//a[@class="dialog-close-button dialog-lightbox-close-button"]')
        # WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(ads))
        # self.browser.find_element(*ads).click()

    def click_element(self, input_locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(input_locator)).click()

    def wait_for_visibility(self, input_locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(input_locator))

    def page_loaded(self) -> None:
        WebDriverWait(self.browser, 10).until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete')

    def element_is_present(self, input_locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(input_locator))
