# Открыть браузер FireFox.
# Перейти на страницу: http://the-internet.herokuapp.com/inputs.
# Ввести в поле текст Sky.
# Очистить это поле (метод clear()).
# Ввести в поле текст Pro.
# Закрыть браузер (метод quit()).

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")
input_element = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input_element.send_keys("Sky")
sleep(5)
input_element.clear()
input_element.send_keys("Pro")
sleep(5)
driver.quit()
