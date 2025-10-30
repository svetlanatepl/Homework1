# Перейдите на сайт
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Получите значение атрибута
# src у 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
waiter = WebDriverWait(browser, 60, 0.1)

browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

content = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

image = browser.find_element(By.CSS_SELECTOR, "img[id='award']")

print(image.get_attribute("src"))

browser.quit()
