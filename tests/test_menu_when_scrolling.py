from pytest import fixture

from pages import Menu


def test_menu_when_scrolling(browser: fixture):
    """Checks that menu elements are present when scrolling the page.
    2. Проверка поведения основного меню в шапке при скроллинге
    - Отображение меню при скроллинге страницы вниз: меню должно оставаться видимым или отображаться корректно после прокрутки страницы.
    - Кликабельность элементов меню при скроллинге: ссылки в меню остаются активными."""
    menu = Menu(browser)
    menu.get_homepage()
    menu.menu_items_are_clickable_when_scrolling()
