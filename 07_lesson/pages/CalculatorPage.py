# Написать автотест для проверки функциональности
# калькулятора на сайте
# https://bonigarcia.dev/# selenium-webdriver-java/slow-calculator.html,
# используя паттерн Page Object.
# Создать класс для страницы калькулятора, который
# будет содержать методы для взаимодействия с элементами:
# Поле ввода задержки (локатор #delay).
# Кнопки калькулятора (цифры, операторы, кнопка =).
# Поле вывода результата.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"


class CalculatorPage:

    def __init__(self, browser):
        # Открываем браузер
        self.browser = browser
        self.wait = WebDriverWait(browser, 5)

    def open(self):
        # Открываем калькулятор на сайте
        self.browser.get(url)

    def delay_input_field(self):
        # Метод Ввода задержки (локатор #delay)
        self.delay_input = self.browser.find_element(By.CSS_SELECTOR, "#delay")
        self.delay_input.clear()
        self.delay_input.send_keys("45")

    def calculator_buttons(self, browser):
        # Метод нажатия кнопок 7, +, 8, =
        self.browser = browser
        self.wait = WebDriverWait(browser, 20)
        self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//span[text()='7']"))).click()
        self.browser.find_element(By.XPATH, "//span[text()='+']").click()
        self.browser.find_element(By.XPATH, "//span[text()='8']").click()
        self.browser.find_element(By.XPATH, "//span[text()='=']").click()

    def get_result(self, browser):
        # Метод вывода результата
        self.browser = browser
        self.wait = WebDriverWait(browser, 45)
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, ".screen"), "15"))
        result = self.browser.find_element(By.CSS_SELECTOR, ".screen").text
        return result
