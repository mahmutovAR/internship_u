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
        except:
            return None
        else:
            return element

    def send_keys_to_element(self, locator: tuple[str, str], data: str) -> None:
        self.get_element_by_locator(locator).send_keys(data)

    def get_current_url(self) -> str:
        return self.driver.current_url

    def get_page_title(self) -> str:
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

    def element_is_clickable(self, locator: tuple[str, str]) -> WebElement | None:
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except:
            return None
        else:
            return element

    def click_element(self, locator: tuple[str, str]) -> None:
        self.element_is_clickable(locator).click()

    def element_is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except:
            return False
        else:
            return True

    def hover_over_element(self, locator: tuple[str, str]):
        actions = ActionChains(self.driver)
        element = self.get_element_by_locator(locator)
        actions.move_to_element(element).perform()
