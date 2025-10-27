# Открыть браузер FireFox.
# Перейти на страницу http://the-internet.herokuapp.com/login.
# В поле username ввести значение tomsmith.
# В поле password ввести значение SuperSecretPassword!.
# Нажать кнопку Login.
# Вывести текст с зеленой плашки в консоль.
# Закрыть браузер (метод quit()).

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
input_username = driver.find_element(By.CSS_SELECTOR, "#username")
input_username.send_keys("tomsmith")
sleep(2)
input_password = driver.find_element(By.CSS_SELECTOR, "#password")
input_password.send_keys("SuperSecretPassword!")
sleep(2)
input_login = driver.find_element(By.CSS_SELECTOR, ".radius")
input_login.click()
sleep(2)
messages = driver.find_element(By.CSS_SELECTOR, "div#flash").text
print(messages)
sleep(2)
driver.quit()
