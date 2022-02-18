from .base_page import BasePage


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
