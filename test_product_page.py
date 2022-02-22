from time import sleep

from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                      marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
    Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
    Ожидаемый результат:
    1) Сообщение о том, что товар добавлен в корзину.
    Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    """
    page = ProductPage(browser, link)  # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.compare_basket_and_product_price()
    page.should_be_price_of_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    """
    Тест, что гость видит кнопку "login" со страницы товара:
    Открываем страницу товара.
    Проверяем, что есть кнопка логина на этой странице.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    Тест, что гость может перейти на страницу регистрации со страницы товара:
    Открываем страницу товара.
    Переходим на страницу регистрации.
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    Тест, что гость видит товар в Корзине, открытой из страницы товара:
    Гость открывает страницу товара
    Переходит в корзину по кнопке в шапке
    Ожидаем, что в корзине нет товаров
    Ожидаем, что есть текст о том что корзина пуста
    """
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_empty()
    page.should_be_text_basket_empty()



class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, email, password):
        """"
        открыть страницу регистрации;
        зарегистрировать нового пользователя;
        проверить, что пользователь залогинен.
        """
        login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(browser):
        """
        Открываем страницу товара
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
        """
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(browser):
        """
        Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
        Ожидаемый результат:
        1) Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
        """
        link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_msg_about_adding()
        page.should_be_add_to_basket_button()
        page.should_be_name_of_product()
        page.compare_basket_and_product_price()
        page.should_be_price_of_product()

#
# def test_temp1(browser, email=None, password=None):
#     login_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
#     page = LoginPage(browser, login_link)
#     page.open()
#     page.register_new_user(email, password)
#     sleep(2)
#     page.should_be_authorized_user()

