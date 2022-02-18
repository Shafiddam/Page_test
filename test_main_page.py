from time import sleep
from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

LINK1 = 'http://selenium1py.pythonanywhere.com/'
LINK2 = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


def test_guest_can_go_to_login_page(browser):
    # LINK = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, LINK1)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, LINK1)
    page.open()
    page.should_be_login_link()


def test_guest_should_be_login_url(browser):
    page = LoginPage(browser, LINK2)
    page.open()
    page.should_be_login_url()


def test_should_be_login_form(browser):
    page = LoginPage(browser, LINK2)
    page.open()
    page.should_be_login_form()


def test_should_be_register_form(browser):
    page = LoginPage(browser, LINK2)
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
