import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url: str) -> None:
        self.driver.get(url)

    def get_element_by_locator(self, locator: tuple[str, str]) -> WebElement | None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
        else:
            return element

    def send_keys_to_element(self, locator: tuple[str, str], data: str) -> None:
        self.get_element_by_locator(locator).send_keys(data)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
        with allure.step('Получить значение "TITLE"'):
            return self.driver.title

    def get_element_text(self, locator: tuple[str, str]) -> str:
        return self.get_element_by_locator(locator).text

    def get_nested_element_text(self, element: tuple[str, str], nested_element: tuple[str, str]) -> str:
        parent_element = self.get_element_by_locator(element)
        return parent_element.find_element(*nested_element).text

    def get_nested_element_link(self, element: tuple[str, str], nested_element: tuple[str, str]) -> str:
        parent_element = self.get_element_by_locator(element)
        return parent_element.find_element(*nested_element).get_attribute('href')

    def scroll_to_element(self, locator: tuple[str, str]) -> None:
        js_code = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_code, self.driver.find_element(*locator))

    def get_clickable_element(self, locator: tuple[str, str]) -> WebElement | None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return None
        else:
            return element

    def click_element(self, locator: tuple[str, str]) -> None:
        self.get_clickable_element(locator).click()

    def element_is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            return True

    def hover_over_element(self, locator: tuple[str, str]):
        actions = ActionChains(self.driver)
        element = self.get_element_by_locator(locator)
        actions.move_to_element(element).perform()

    def get_cookies_data(self) -> list:
        return self.driver.get_cookies()

    def load_cookies_data(self, cookies: list) -> None:
        for data in cookies:
            self.driver.add_cookie(data)

    def refresh_page(self) -> None:
        self.driver.refresh()

    def get_active_element(self) -> WebElement:
        return self.driver.switch_to.active_element

    def blur_element(self, locator: tuple[str, str]) -> None:
        self.driver.execute_script("arguments[0].blur();", self.get_element_by_locator(locator))

    def page_has_scroll(self) -> bool:
        compare_body_heights = "return document.body.scrollHeight > document.body.clientHeight;"
        compare_html_heights = "return document.documentElement.scrollHeight > document.documentElement.clientHeight;"
        if self.driver.execute_script(compare_body_heights) or self.driver.execute_script(compare_html_heights):
            return True
        return False
