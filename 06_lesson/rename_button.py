# Перейдите на сайт http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и
# выведите в консоль "SkyPro".

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
waiter = WebDriverWait(browser, 40, 0.1)

browser.get("http://uitestingplayground.com/textinput")

input_element = browser.find_element(By.CSS_SELECTOR, "#newButtonName")
input_element.send_keys("SkyPro")

button_click = browser.find_element(By.CSS_SELECTOR, "#updatingButton").click()

content = waiter.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#updatingButton"))
)
txt = content.text

print(txt)
browser.quit()
