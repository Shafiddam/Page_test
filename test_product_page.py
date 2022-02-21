from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import pytest

# первый линк:
# LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# второй (новый) линк:
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
# третий линк (без промо-акций), для ОТРИЦАТЕЛЬНЫХ проверок :
LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207'


@pytest.mark.skip
# @pytest.mark.parametrize('LINK', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, LINK):
    """
    Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
    Ожидаемый результат:
    1) Сообщение о том, что товар добавлен в корзину.
    Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
    2) Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    """
    page = ProductPage(browser, LINK)  # инициализируем Page Object,
    # передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
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
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    """
    Открываем страницу товара
    Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    Открываем страницу товара
    Добавляем товар в корзину
    Проверяем, что нет сообщения об успехе с помощью is_disappeared
    """
    page = ProductPage(browser, LINK)
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
