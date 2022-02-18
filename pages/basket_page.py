from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        """
        Ожидаем, что в корзине нет товаров (локатор  PRODUCTS_IN_BASKET h2.col-sm-6.h3)
        """
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "BASKET IS NOT EMPTY"

    def should_be_text_basket_empty(self):
        """
        Ожидаем, что есть текст о том что корзина пуста (локатор div#content_inner p)
        Ожидаем, что в корзине нет товаров
        """
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), "BASKET IS NOT EMPTY"
