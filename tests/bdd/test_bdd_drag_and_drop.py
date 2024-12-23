import pytest
from pytest import fixture
from pytest_bdd import scenarios, given, when, then

from pages import DragAndDropPage


scenarios('./features/drag_and_drop.feature')


@pytest.fixture
def drag_and_drop(browser: fixture):
    return DragAndDropPage(browser)


@given('DragAndDrop page')
def open_page(drag_and_drop: fixture):
    drag_and_drop.open_page()


@when('Drag and drop element into specified area')
def drag_element(drag_and_drop: fixture):
    drag_and_drop.switch_to_iframe()
    drag_and_drop.check_droppable_label_before_action()
    drag_and_drop.drag_and_drop_action()


@then('After "Drag and Drop" action text in specified area changed')
def drop_element(drag_and_drop: fixture):
    drag_and_drop.check_droppable_label_after_action()


