import allure
from allure import severity_level
from pytest import fixture

from pages import DragAndDropPage


@allure.severity(severity_level.NORMAL)
@allure.epic("Smoke тест")
@allure.feature("Drag and Drop")
@allure.testcase("Задача U10")
@allure.story("Перетащить элемент в принимающий")
@allure.title("Перемещение элемента на странице")
@allure.description(
    """
    Цель: Проверить работу перемещения элемента

    Предусловие:
        - Открыть браузер

    Шаги:
        1. Открыть страницу
        2. Проверить текст принимающего элемента до перемещения
        3. Переместить элемент в принимающий
        4. Проверить текст принимающего элемента после перемещения

    Ожидаемый результат:
        - После успешного перемещения текст в принимающем элементе изменился""")
def test_drag_and_drop(browser: fixture):
    drag_and_drop_page = DragAndDropPage(browser)
    drag_and_drop_page.open_page()
    drag_and_drop_page.switch_to_iframe()
    drag_and_drop_page.check_droppable_label_before_action()
    drag_and_drop_page.drag_and_drop_action()
    drag_and_drop_page.check_droppable_label_after_action()

