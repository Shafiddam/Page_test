import math
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.wait import WebDriverWait
from .locators import BasePageLocators, ProductPageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        """
        Конструктор — метод, который вызывается, когда мы создаем объект.
        Конструктор объявляется ключевым словом __init__.
        В него в качестве параметров мы передаем экземпляр драйвера и url адрес.
        Внутри конструктора сохраняем эти данные как аттрибуты нашего класса
        """
        self.browser = browser
        self.url = url

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket(self):
        """ Находим кнопку корзины и переходим в корзину """
        link = self.browser.find_element(*BasePageLocators.BASKET_BTN)
        link.click()

    def is_element_present(self, how, what):
        """
        Метод, в котором будем перехватывать исключение. В него будем передавать два аргумента:
        как искать (css, id, xpath и тд) и собственно что искать (строку-селектор).
        Чтобы перехватывать исключение, нужна конструкция try/except:
        """
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        """
        Абстрактный метод, который проверяет, ___ЧТО ЭЛЕМЕНТ НЕ ПОЯВЛЯЕТСЯ___
        на странице в течение заданного времени:
        """
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        """
        Метод, который проверяет, ___ЧТО ЭЛЕМЕНТ ИСЧЕЗАЕТ___
        Следует воспользоваться явным ожиданием вместе с функцией until_not,
        в зависимости от того, какой результат мы ожидаем:
        """
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def open(self):
        """ Открытие браузера """
        self.browser.get(self.url)

    def should_be_login_link(self):
        """ Проверка, что подстрока "login" есть в текущем url браузера """
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "LOGIN LINK IS NOT PRESENTED"

    def solve_quiz_and_get_code(self):
        """
        вспомогательная функция вычисления формулы и ввода ответа
        во всплывающее поле alert'a по ссылке промокода:
        """
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"YOUR CODE: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("NO SECOND ALERT PRESENTED")
