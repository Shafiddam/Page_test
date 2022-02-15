from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
from time import sleep
import pytest

# первый линк:
# LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
# второй (новый) линк:
# LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'


@pytest.mark.parametrize('LINK', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, LINK):
    """
           Проверка нажатия на кнопку ADD_TO_BASKET_BUTTON
           Ожидаемый результат:
           1)Сообщение о том, что товар добавлен в корзину. Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
           2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    """
    page = ProductPage(browser, LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    # page.should_be_msg_about_adding()
    # print("\n 1) SHOULD_BE_MSG_ABOUT_ADDING")
    # page.should_be_add_to_basket_button()
    # print("\n 2) SHOULD_BE_ADD_TO_BASKET_BUTTON")
    # page.should_be_name_of_product()
    # print("\n 3) SHOULD_BE_NAME_OF_PRODUCT")
    # page.compare_basket_and_product_price()
    # print("\n 4) COMPARE_BASKET_AND_PRODUCT_PRICE")
    # # page.should_be_msg_about_adding()
    # page.should_be_price_of_product()
    # print("\n 5) SHOULD_BE_PRICE_OF_PRODUCT")



'''
# ниже 5 тестов, но вставили их в один тест "test_guest_can_add_product_to_basket":
def test_should_be_add_to_basket_button(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_button()

def test_should_be_name_of_product(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_of_product()

def test_compare_basket_and_product_price(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_basket_and_product_price()

def test_should_be_msg_about_adding(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()

def test_should_be_price_of_product(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_price_of_product()
'''