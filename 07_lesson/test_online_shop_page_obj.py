# Написать тест, который использует PageObject для выполнения
# следующих действий:
# Открыть сайт магазина.
# Авторизоваться как пользователь standard_user.
# Добавить в корзину товары:
# Sauce Labs Backpack. Sauce Labs Bolt T-Shirt. Sauce Labs Onesie.
# Перейти в корзину. Нажать кнопку Checkout.
# Заполнить форму своими данными:
# Имя. Фамилия. Почтовый индекс.
# Прочитать со страницы итоговую стоимость (Total).
# Закрыть браузер.
# Проверить (assert), что итоговая сумма равна $58.29.

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
from pages.OnlineshopPage import LoginPage
from pages.OnlineshopPage import MainPage
from pages.OnlineshopPage import CartPage
from pages.OnlineshopPage import BuyPage


@pytest.fixture
def browser():
    # Определяем опции браузера
    chrome_options = Options()

    # Включаем режим инкогнито
    chrome_options.add_argument('--incognito')

    # Инициализация драйвера с нужными опциями
    # browser = webdriver.Chrome(service=ChromeService(
    #     ChromeDriverManager().install()), options=chrome_options)
    chrome_driver_path = r"D:\Skypro\chromedriver-win64\chromedriver.exe"
    browser = webdriver.Chrome(service=ChromeService(
        chrome_driver_path), options=chrome_options)

    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_online_shop(browser):
    login_page = LoginPage(browser)

    # Открываем интернет-магазин
    login_page.open()

    # Авторизация
    login_page.login_page(browser)
    login_page.login_click_button(browser)

    main_page = MainPage(browser)

    # Добавление товара в корзину
    main_page.add_to_cart()

    # Переход в корзину
    main_page.go_to_cart(browser)

    cart_page = CartPage(browser)

    # Проверяем содержимое корзины
    cart_items = cart_page.get_cart_items()
    expected_items = [
        {'name': 'Sauce Labs Backpack', 'price': '$29.99'},
        {'name': 'Sauce Labs Bolt T-Shirt', 'price': '$15.99'},
        {'name': 'Sauce Labs Onesie', 'price': '$7.99'}
    ]
    assert cart_items == expected_items

    # Нажимаем кнопку Checkout
    cart_page.click_button()

    buy_page = BuyPage(browser)

    # заполнение формы данными
    buy_page.fill_form()
    buy_page.click_button_form()

    # Итоговая стоимость
    total_element = buy_page.get_cart_total()
    assert total_element == "Total: $58.29"
