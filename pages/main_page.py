# from selenium.webdriver.common.by import By
from .base_page import BasePage
# from .locators import MainPageLocators
# from .login_page import LoginPage


class MainPage(BasePage):
    """
    ПЕРЕНЕСЛИ ДВА МЕТОДА В БАЗУ BASE_PAGE.PY, ТУТ СТАВИМ "ЗАГЛУШКУ":
    Метод __init__ вызывается при создании объекта.
    Конструктор с ключевым словом super на самом деле только вызывает
    конструктор класса предка и передает ему все те аргументы, которые мы передали в конструктор mainpage.

    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # alert = self.browser.switch_to.alert
        # alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "LOGIN LINK IS NOT PRESENTED"
    """
    def __init__(self, *args, **kwargs):
                super(MainPage, self).__init__(*args, **kwargs)
    # или можно не городить эту конструкцию, а просто написать pass:
    # pass

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self):
        """
            Гость открывает главную страницу
            Переходит в корзину по кнопке в шапке сайта
            Ожидаем, что в корзине нет товаров
            Ожидаем, что есть текст о том что корзина пуста
        """

