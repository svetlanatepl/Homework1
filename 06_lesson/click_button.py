# Перейдите на страницу http://uitestingplayground.com/ajax.
# Нажмите на синюю кнопку.
# Получите текст из зеленой плашки.
# Выведите его в консоль
# "Data loaded with AJAX get request."

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.implicitly_wait(20)

browser.get("http://www.uitestingplayground.com/ajax")
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

content = browser.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

print(txt)

browser.quit()
