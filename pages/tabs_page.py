import allure

from data import PageUrls
from locators import TabsLocators
from . import BasePage


class TabsPage(BasePage):
    def open_page(self) -> None:
        with allure.step('Открыть страницу'):
            self.open_url(PageUrls.tabs_page)

    def switch_to_iframe(self) -> None:
        self.switch_to_iframe_by_locator(TabsLocators.iframe)

    def click_link(self) -> None:
        with allure.step('Нажать на ссылку'):
            self.click_element(TabsLocators.link)

    def get_current_window_handles(self) -> list:
        with allure.step('Получить дескрипторы окна'):
            return self.get_window_handles()

    def switch_to_new_tab(self, tab_id: str) -> None:
        with allure.step('Перейти на новую вкладку'):
            self.switch_to_tab(tab_id)
