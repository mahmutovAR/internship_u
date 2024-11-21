from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.homepage = 'https://www.way2automation.com/'
        self.login_page = 'https://www.way2automation.com/angularjs-protractor/registeration/#/login'
        self.registration_page = 'https://www.way2automation.com/way2auto_jquery/registration.php#load_box'
        self.ads_locator = (By.XPATH, '//div[@class="elementor-widget-wrap elementor-element-populated lazyloaded"]')

    def get_homepage(self) -> None:
        self.browser.get(self.homepage)

    def get_login_page(self) -> None:
        self.browser.get(self.login_page)

    def get_registration_page(self) -> None:
        self.browser.get(self.registration_page)

    def get_element_by_locator(self, locator: tuple[str, str]) -> WebElement:
        return self.browser.find_element(*locator)

    def get_current_url(self) -> str:
        return self.browser.current_url

    def scroll_to_element(self, locator: tuple[str, str]):
        js_code = "arguments[0].scrollIntoView();"
        self.browser.execute_script(js_code, self.browser.find_element(*locator))

    def scroll_page(self):
        self.browser.execute_script("window.scrollBy(0, 3500);")

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

    def click_element(self, locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(locator)).click()

    def wait_for_visibility(self, locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))

    def last_page_element_loaded(self, locator: tuple[str, str]) -> None:
        self.browser.find_element(*locator)

    def element_is_present(self, locator: tuple[str, str]) -> None:
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(locator))
