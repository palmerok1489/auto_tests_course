import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/selects1.html'

def calc(x,y) -> str:
    return str(int(x) + int(y))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num_element1 = browser.find_element(By.ID, 'num1')
    x = num_element1.text
    num_element2 = browser.find_element(By.ID, 'num2')
    y = num_element2.text
    res = calc(x,y)
    
    input = browser.find_element(By.TAG_NAME, 'select').click()
    select = Select(browser.find_element(By.TAG_NAME,'select'))
    select.select_by_value(res)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()