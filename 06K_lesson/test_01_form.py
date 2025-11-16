# Откройте страницу:
# https://bonigarcia.dev/selenium-webdriver-java/data-types.html
# в Edge или Safari.
# Заполните форму значениями:
# First name = Иван, Last name = Петров
# Address = Ленина, 55-3, Email = test@skypro.com
# Phone number = +7985899998787
# Zip code *оставить пустым
# City = Москва, Country = Россия
# Job position = QA, Company = SkyPro
# Нажмите кнопку Submit.
# Проверьте (assert), что поле Zip code
# подсвечено красным.
# Проверьте (assert), что остальные поля подсвечены зеленым.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService


def test_form():
    edge_driver_path = r"C:\Users\Admin\edgedriver_win64\msedgedriver.exe"
    driver = webdriver.Edge(service=EdgeService(edge_driver_path))
    driver.maximize_window()

    try:
        # Шаг 1: Открываем нужную страницу
        driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
        )

        # Шаг 2: Заполняем форму
        wait = WebDriverWait(driver, 40)
        wait.until(EC.presence_of_element_located(
            (By.NAME, "first-name")
        )).send_keys("Иван")
        driver.find_element(
             By.CSS_SELECTOR, "input[name='last-name']").send_keys('Петров')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='address']"
        ).send_keys('Ленина, 55-3')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='e-mail']"
        ).send_keys('test@skypro.com')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='phone']"
        ).send_keys('+7985899998787')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='city']").send_keys('Москва')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='country']").send_keys('Россия')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='job-position']").send_keys('QA')
        driver.find_element(
             By.CSS_SELECTOR, "input[name='company']").send_keys('SkyPro')

        # Шаг 3: Нажимаем кнопку Submit
        submit_button = wait.until(EC.element_to_be_clickable(
             (By.CSS_SELECTOR, "button[type='submit']")
        ))
        submit_button.click()

        # Шаг 4: Проверяем подсветку полей
        zip_code_field = driver.find_element(By.ID, 'zip-code')
        assert "alert py-2 alert-danger" \
            in zip_code_field.get_attribute("class")

        # Проверка остальных полей на зеленую подсветку
        fields = driver.find_elements(By.CSS_SELECTOR, "input")
        for field in fields:
            if field != zip_code_field:
                assert "success" in field.get_attribute("class"), \
                    f"Поле {field.get_attribute('name')} не подсвечено зеленым"

    finally:
        # Закрываем браузер
        driver.quit()
