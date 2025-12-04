# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
# Авторизуйтесь как пользователь standard_user.
# Добавьте в корзину товары:
# Sauce Labs Backpack. Sauce Labs Bolt T-Shirt. Sauce Labs Onesie.
# Перейдите в корзину. Нажмите Checkout.
# Заполните форму своими данными: имя, фамилия, почтовый индекс.
# Нажмите кнопку Continue.
# Прочитайте со страницы итоговую стоимость (Total). Закройте браузер.
# Проверьте, что итоговая сумма равна $58.29.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 60, 0.1)
    driver.get("https://www.saucedemo.com/")

    # Авторизуемся
    username_input = driver.find_element(By.CSS_SELECTOR, "#user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.CSS_SELECTOR, "#password")
    password_input.send_keys("secret_sauce")

    login_button = wait.until(EC.element_to_be_clickable(
                                (By.CSS_SELECTOR, "#login-button")))
    login_button.click()

    # Добавляем товары в корзину
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack")
    )).click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()

    driver.find_element(
        By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()

    # Переходим в корзину и нажимаем Checkout
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[data-test='shopping-cart-link']")
        )
    ).click()
    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполняем ворму данными: имя, фамилия, почтовый индекс
    first_name = driver.find_element(By.CSS_SELECTOR, "#first-name")
    first_name.send_keys("Svetlana")
    last_name = driver.find_element(By.CSS_SELECTOR, "#last-name")
    last_name.send_keys("Telyakova")
    postal_code = driver.find_element(By.CSS_SELECTOR, "#postal-code")
    postal_code.send_keys("427960")

    # Нажимаем Continue
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "#continue")
        )
    ).click()

    # Проверяем итоговую стоимость Total
    sum = driver.find_element(By.CLASS_NAME, "summary_total_label")
    total_price = sum.text
    driver.quit()
    assert total_price == "Total: $58.29"
