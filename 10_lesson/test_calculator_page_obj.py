# Написать тест, который использует PageObject для выполнения
# следующих действий:
# Открыть страницу калькулятора.
# Ввести значение 45 в поле задержки (локатор #delay).
# Нажать кнопки:
# 7, +, 8, =.
# Проверить (assert), что в окне отобразится результат 15 через 45 секунд.

import pytest
from selenium import webdriver
from pages.CalculatorPage import CalculatorPage
import allure


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.title("Тестирование калькулятора")
@allure.description("Тест проверяет корректность работы калькулятора.")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_form_calculator(browser):
    """
    Тест проверяет работу калькулятора.

    :type browser: WebDriver — объект драйвера Selenium.
    """
    calculator_page = CalculatorPage(browser)
    # Открытие страницы калькулятора
    calculator_page.open()

    # Установка задержки (в секундах)
    calculator_page.delay_input_field(45)

    # Нажатие кнопок
    calculator_page.calculator_buttons(browser)

    # Получение результата
    res = calculator_page.get_result(browser)

    with allure.step("Проверка результата"):
        assert res == "15"
