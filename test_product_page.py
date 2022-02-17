import time
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.base_page import BasePage
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
        1)Сообщение о том, что товар добавлен в корзину.
        Название товара в сообщении должно совпадать с тем товаром, который вы действительно добавили.
        2)Сообщение со стоимостью корзины. Стоимость корзины совпадает с ценой товара.
    """
    page = ProductPage(browser,
                       LINK)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    print("\n TEST #SHOULD_BE_MSG_ABOUT_ADDING")
    page.should_be_msg_about_adding()
    print("\n TEST #SHOULD_BE_ADD_TO_BASKET_BUTTON")
    page.should_be_add_to_basket_button()
    print("\n TEST #SHOULD_BE_NAME_OF_PRODUCT")
    page.should_be_name_of_product()
    print("\n TEST #COMPARE_BASKET_AND_PRODUCT_PRICE")
    page.compare_basket_and_product_price()
    print("\n TEST #SHOULD_BE_PRICE_OF_PRODUCT")
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
    # time.sleep(5)


def test_guest_cant_see_success_message(browser):
    """
        Открываем страницу товара
        Проверяем, что нет сообщения об успехе с помощью is_not_element_present
    """
    page = ProductPage(browser, LINK)
    page.open()
    page.should_not_be_success_message()
    # time.sleep(5)


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




'''
# ниже 5 тестов, но вставил их в один тест "test_guest_can_add_product_to_basket", 
# промаркирую их skip'ом для пропуска

@pytest.mark.skip
def test_should_be_add_to_basket_button(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_add_to_basket_button()


@pytest.mark.skip
def test_should_be_name_of_product(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_of_product()


@pytest.mark.skip
def test_compare_basket_and_product_price(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_basket_and_product_price()


@pytest.mark.skip
def test_should_be_msg_about_adding(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()


@pytest.mark.skip
def test_should_be_price_of_product(browser):
    page = ProductPage(browser, LINK)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_price_of_product()
'''
