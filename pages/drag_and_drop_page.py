import allure

from data import PageUrls
from locators import DragAndDropLocators
from . import BasePage


class DragAndDropPage(BasePage):
    def open_page(self) -> None:
        with allure.step('Открыть страницу'):
            self.open_url(PageUrls.drag_and_drop_page)

    def switch_to_iframe(self) -> None:
        self.switch_to_iframe_by_locator(DragAndDropLocators.iframe)

    def check_droppable_label_before_action(self) -> None:
        with allure.step('Проверить текст принимающего элемента до перемещения'):
            expected = 'Drop here'
            text = self.get_element_text(DragAndDropLocators.droppable_area)
            assert text == expected, f'Expected label "{expected}", but got "{text}"'

    def drag_and_drop_action(self) -> None:
        with allure.step('Переместить элемент в принимающий'):
            self.drag_and_drop_element(DragAndDropLocators.draggable_box, DragAndDropLocators.droppable_area)

    def check_droppable_label_after_action(self) -> None:
        with allure.step('Проверить текст принимающего элемента после перемещения'):
            expected = 'Dropped!'
            text = self.get_element_text(DragAndDropLocators.droppable_area)
            assert text == expected, f'Expected label "{expected}", but got "{text}"'
