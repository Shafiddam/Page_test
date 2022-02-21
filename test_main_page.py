from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link1 = 'http://selenium1py.pythonanywhere.com/'
link2 = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def test_guest_can_go_to_login_page(browser):
    """
    Тест, что гость может перейти на страницу логина:
    Гость открывает главную страницу.
    Кликает на кнопку логина.
    """
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    """ Тест, что есть форма регистрации на странице. """
    page = MainPage(browser, link1)
    page.open()
    page.should_be_login_link()


def test_guest_should_be_login_url(browser):
    """ Тест, что ссылка логина корректная. """
    page = LoginPage(browser, link2)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    """ Тест, что есть форма логина на странице. """
    page = LoginPage(browser, link2)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    """ Тест, что есть форма регистрации на странице. """
    page = LoginPage(browser, link2)
    page.open()
    page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    Гость открывает главную страницу
    Переходит в корзину по кнопке в шапке сайта
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = 'http://selenium1py.pythonanywhere.com/ru'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_empty()
    page.should_be_text_basket_empty()
