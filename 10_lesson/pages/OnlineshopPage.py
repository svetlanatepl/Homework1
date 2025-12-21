# написать автотест для проверки функциональности интернет-магазина на
# сайте https://www.saucedemo.com/, используя паттерн Page Object.
# Создать класс для страницы авторизации, который будет содержать
# методы для ввода логина и пароля, а также для нажатия кнопки входа.
# Создать класс для главной страницы магазина, который будет содержать
# методы для добавления товаров в корзину и перехода в корзину.
# Создать класс для страницы корзины, который будет содержать методы
# для нажатия кнопки Checkout и проверки содержимого корзины.
# Создать класс для страницы оформления заказа, который будет
# содержать методы для заполнения формы данными
# (имя, фамилия, почтовый индекс) и проверки итоговой стоимости.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginPage:
    """
    Класс для страницы авторизации
    """

    def __init__(self, browser):
        """
        Конструктор класса LoginPage

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    @allure.step("Открытие страницы интернет-магазина")
    def open(self):
        """
        Открываем интернет-магазин
        """
        url = "https://www.saucedemo.com/"
        self.browser.get(url)

    @allure.step("Авторизация")
    def login_page(self, browser):
        """
        Авторизация

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        username_input = self.browser.find_element(
            By.CSS_SELECTOR, "#user-name")
        username_input.send_keys("standard_user")

        password_input = self.browser.find_element(
            By.CSS_SELECTOR, "#password")
        password_input.send_keys("secret_sauce")

    @allure.step("Нажатие кнопки login-button")
    def login_click_button(self, browser):
        """
        Нажатие кнопки для входа

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)
        login_button = self.wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, "#login-button")))
        login_button.click()


class MainPage:
    """
    Класс для главной страницы магазина
    """

    def __init__(self, browser):
        """
        Конструктор класса MainPage

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    @allure.step("Добавление товара в корзину")
    def add_to_cart(self):
        """
        Добавляем товары в корзину
        """
        self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
        )).click()

        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
        ).click()

        self.browser.find_element(
            By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    @allure.step("Переходим в корзину")
    def go_to_cart(self, browser):
        """
        Переходим в корзину
        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)
        self.wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
            )
        ).click()


class CartPage:
    """
    Класс для страницы корзины
    """

    def __init__(self, browser):
        """
        Конструктор класса CartPage

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser

    @allure.step("Получаем название и цену товара")
    def get_cart_items(self) -> list:
        """
        Метод возвращает информацию о названии и цене товара.

        Returns:
            list, возвращает список с названием и ценой товара
        """
        items = []
        # Предположим, что товары в корзине имеют класс 'cart_item_label'
        cart_item_elements = self.browser.find_elements(
            By.CLASS_NAME, 'cart_item_label')
        for item in cart_item_elements:
            # Получаем название и цену товара
            name = item.find_element(
                By.CLASS_NAME, 'inventory_item_name').text
            price = item.find_element(
                By.CLASS_NAME, 'inventory_item_price').text
            items.append({'name': name, 'price': price})
        return items

    @allure.step("Нажимаем на кнопку Checkout")
    def click_button(self):
        """
        Метод нажатия кнопки Checkout
        """
        self.browser.find_element(By.CSS_SELECTOR, "#checkout").click()


class BuyPage:
    """
    Класс для страницы оформления заказа
    """

    def __init__(self, browser):
        """
        Конструктор класса BuyPage

        :param browser: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser
        self.fields = {
            'firstName': "Svetlana",
            'lastName': "Telyakova",
            'postalCode': "427960"
        }

    @allure.step("Заполнение формы данными")
    def fill_form(self):
        """
        Метод для автоматического заполнения формы данными
        """
        self.wait = WebDriverWait(self.browser, 20)
        for field, value in self.fields.items():
            self.wait.until(
                EC.presence_of_element_located((
                    By.NAME, field))).send_keys(value)

    @allure.step("Нажимаем кнопку Continue")
    def click_button_form(self):
        """
        Метод нажатия кнопки Continue
        """
        self.browser.find_element(By.CSS_SELECTOR, "#continue").click()

        # Нажимаем Continue
    #     WebDriverWait(self.browser, 20).until(
    #         EC.element_to_be_clickable(
    #             (By.CSS_SELECTOR, "#continue"))
    # ).click()

    @allure.step("Поиск элемента с итоговой стоимостью")
    def get_cart_total(self):
        """
        Находим элемент с итоговой стоимостью
        Returns:
            float, возвращает итоговую стоимость
        """
        total_element = self.browser.find_element(
            By.CLASS_NAME, "summary_total_label").text
        return total_element
