from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        """ Добавление товара в корзину """
        btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn.click()

    def compare_basket_and_product_price(self):
        """ Сравнение цен товара и пустой корзины """
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, "PRODUCT PRICE AND BASKET PRICE IS NOT EQUAL"

    def message_disappeared_after_adding_product_to_basket(self):
        """ Проверка ___ЧТО ЭЛЕМЕНТ ИСЧЕЗАЕТ___ после добавления в корзину """
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "SUCCESS MESSAGE IS DISAPPEARED_AFTER_ADDING, BUT SHOULD NOT BE"

    def should_be_add_to_basket_button(self):
        """ Проверка, что есть кнопка 'ДОБАВИТЬ В КОРЗИНУ' """
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "BTN_ADD_TO_BASKET NOT FOUND"

    def should_be_name_of_product(self):
        """ Проверка наличия имени продукта(товара) """
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), "PRODUCT NAME NOT FOUND"

    def should_be_price_of_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), "PRODUCT PRICE NOT FOUND"

    def should_be_msg_about_adding(self):
        """ Проверка выхода сообщения, что товар добавлен """
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message, "PRODUCT NAME NOT FOUND ON MESSAGE"

    def should_not_be_success_message(self):
        """ Проверка ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ на странице в течение заданного времени """
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "SUCCESS MESSAGE IS PRESENTED, BUT SHOULD NOT BE"
