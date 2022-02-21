from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        """ Кажется тут прописаны "заглушки" """
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ Проверка на корректный url адрес. """
        assert '/login' in self.browser.current_url, "LOGIN_LINK IS FALSE"

    def should_be_login_form(self):
        """ Проверка, что есть форма логина. """
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM IS NOT PRESENTED"

    def should_be_register_form(self):
        """ Проверка, что есть форма регистрации на странице. """
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM IS NOT PRESENTED"
