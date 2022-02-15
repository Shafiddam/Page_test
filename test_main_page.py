from time import sleep
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

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
