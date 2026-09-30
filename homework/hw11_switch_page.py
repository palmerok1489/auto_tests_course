import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = 'https://suninjuly.github.io/redirect_accept.html'

def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element(By.CSS_SELECTOR, '.trollface.btn.btn-primary')
    button.click()
    
    #переход на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    input = browser.find_element(By.ID, 'input_value')
    x = input.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    
    button1 = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    button1.click()
    
finally:
    time.sleep(10)
    browser.quit()