import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = 'https://suninjuly.github.io/execute_script.html'

def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    
    input = browser.find_element(By.ID, 'answer')
    input.send_keys(y)
    input1 = browser.find_element(By.ID, 'robotCheckbox')
    input1.click()
    input2 = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("window.scrollBy(0, 100);")
    input2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()