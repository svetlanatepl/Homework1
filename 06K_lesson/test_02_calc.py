# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
# в Google Chrome.
# В поле ввода по локатору #delay
# введите значение 45.
# Нажмите на кнопки:
# 7 + 8 =
# Проверьте (assert), что в окне отобразится
# результат 15 через 45 секунд.

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 45, 0.1)

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

    wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//span[text()='7']"))).click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    wait.until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"))
    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15"

    # Закрываем браузер
    driver.quit()
