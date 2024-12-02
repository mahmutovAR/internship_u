import allure

from data import PageUrls
from locators import AlertsLocators
from . import BasePage


class AlertsPage(BasePage):
    def open_page(self) -> None:
        with allure.step('Открыть страницу'):
            self.open_url(PageUrls.alerts_page)

    def click_input_alert(self) -> None:
        with allure.step('Нажать "Input Alert"'):
            self.click_element(AlertsLocators.input_alert)

    def switch_to_iframe(self) -> None:
        self.switch_to_iframe_by_locator(AlertsLocators.iframe)

    def click_input_box(self) -> None:
        with allure.step('Нажать кнопку для вызова "Input box"'):
            self.click_element(AlertsLocators.input_box)

    def input_text(self, text: str) -> None:
        with allure.step('Ввести текст'):
            self.send_keys_to_alert(text)

    def get_text(self) -> str:
        return self.get_element_text(AlertsLocators.message)
