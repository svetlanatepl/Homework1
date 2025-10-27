# Клик по кнопке без ID.
# Открыть браузер Google Chrome.
# Перейти на страницу: http://uitestingplayground.com/dynamicid.
# Кликнуть на синюю кнопку.

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://uitestingplayground.com/dynamicid")
check_input = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
check_input.click()
sleep(5)
