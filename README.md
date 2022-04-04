Windows 10, Python 3.10, Google Chrome 98.0.4758.102

# Page_test
base_page.py - тут мы храним методы, которые применяются по всему проекту вообще.  
locators.py - тут мы храним локаторы, в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать.  
main_page.py - тут мы храним методы по конкретной странице, завернутые в класс этой странице.  
test_main_page.py:  
  """
  тест-кейсы для главной страницы (например тесты регистрации), которые будем запускать с помощью pytest. Мы будем создавать функции, которым:  
  1) выдаём нужный для проверки линк
  2) создаём в функции переменную page, которой передаём браузер из base_page.py(класс BasePage) и линк из шага 1)
  3) добавляем проверки, которые создавали методами в main_page.py
  """

test_product_page.py:
  """
  тесты для товара(продукта), например добавление в корзину 
  """
