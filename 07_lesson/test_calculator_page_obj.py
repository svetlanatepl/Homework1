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


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.maximize_window()
    yield browser
    browser.quit()


def test_form_calculator(browser):
    calculator_page = CalculatorPage(browser)
    calculator_page.open()
    calculator_page.delay_input_field()
    calculator_page.calculator_buttons(browser)
    res = calculator_page.get_result(browser)

    # проверка результата
    assert res == "15"
