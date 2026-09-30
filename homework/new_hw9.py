import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 


link = "https://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Ivan")
    
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Smolensk@mai.com")
    
    input4 = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    input4.send_keys(file_path)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()