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
        """Opens specified page."""
        self.driver.get(url)

    def get_element_by_locator(self, locator: tuple[str, str]) -> WebElement | None:
        """Returns page element by specified locator if it is presented on the page."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return None
        else:
            return element

    def send_keys_to_element(self, locator: tuple[str, str], data: str) -> None:
        """Fills in data into input field."""
        self.get_element_by_locator(locator).send_keys(data)

    def get_current_url(self) -> str:
        """Returns current page url."""
        return self.driver.current_url

    def get_page_title(self) -> str:
        """Returns current page title."""
        with allure.step('Получить значение "TITLE"'):
            return self.driver.title

    def get_element_text(self, locator: tuple[str, str]) -> str:
        """Returns specified page element text."""
        return self.get_element_by_locator(locator).text

    def get_nested_element_text(self, element: tuple[str, str], nested_element: tuple[str, str]) -> str:
        """Returns nested page element text."""
        parent_element = self.get_element_by_locator(element)
        return parent_element.find_element(*nested_element).text

    def get_nested_element_link(self, element: tuple[str, str], nested_element: tuple[str, str]) -> str:
        """Returns nested page element link."""
        parent_element = self.get_element_by_locator(element)
        return parent_element.find_element(*nested_element).get_attribute('href')

    def scroll_to_element(self, locator: tuple[str, str]) -> None:
        """Scrolls to specified page element."""
        js_code = "arguments[0].scrollIntoView();"
        self.driver.execute_script(js_code, self.driver.find_element(*locator))

    def get_clickable_element(self, locator: tuple[str, str]) -> WebElement | None:
        """Returns page element if it is clickable."""
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            return None
        else:
            return element

    def click_element(self, locator: tuple[str, str]) -> None:
        """Clicks specified page element."""
        self.get_clickable_element(locator).click()

    def element_is_visible(self, locator: tuple[str, str]) -> bool:
        """Checks if specified page element is visible."""
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        else:
            return True

    def hover_over_element(self, locator: tuple[str, str]):
        """Hovers over specified element."""
        actions = ActionChains(self.driver)
        element = self.get_element_by_locator(locator)
        actions.move_to_element(element).perform()

    def get_cookies_data(self) -> list:
        """Returns cookies."""
        return self.driver.get_cookies()

    def delete_cookies_data(self) -> list:
        """Deletes cookies."""
        return self.driver.delete_all_cookies()

    def load_cookies_data(self, cookies: list) -> None:
        """Loads cookies."""
        for data in cookies:
            self.driver.add_cookie(data)

    def refresh_page(self) -> None:
        """Refreshes current page."""
        self.driver.refresh()

    def get_active_element(self) -> WebElement:
        """Switches to page active element and returns it."""
        return self.driver.switch_to.active_element

    def blur_element(self, locator: tuple[str, str]) -> None:
        """Blurs specified page element."""
        self.driver.execute_script("arguments[0].blur();", self.get_element_by_locator(locator))

    def page_has_scroll(self) -> bool:
        """Checks if page has vertical scroll."""
        return self.driver.execute_script("return document.documentElement.scrollHeight > document.documentElement.clientHeight;")

    def switch_to_iframe_by_locator(self, locator: tuple[str, str]) -> None:
        """Switches to iframe by specified locator."""
        iframe = self.get_element_by_locator(locator)
        self.driver.switch_to.frame(iframe)

    def drag_and_drop_element(self, draggable_element: tuple[str, str],
                              droppable_element: tuple[str, str]) -> None:
        """Drags element to drop area."""
        draggable = self.get_element_by_locator(draggable_element)
        droppable = self.get_element_by_locator(droppable_element)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable, droppable).perform()

    def get_window_handles(self) -> list:
        """Returns window handles list."""
        return self.driver.window_handles

    def switch_to_tab(self, tab_id: str) -> None:
        """Switches to the specified tab."""
        self.driver.switch_to.window(tab_id)

    def send_keys_to_alert(self, data: str) -> None:
        """Fills in data into alert input field."""
        alert = WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert.send_keys(data)
        alert.accept()
