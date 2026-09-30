import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'https://suninjuly.github.io/explicit_wait2.html'

def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    #browser.implicitly_wait(12)
    #browser.get("https://suninjuly.github.io/explicit_wait2.html")
    
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    button = browser.find_element(By.ID, 'book')
    button.click()
    
    input = browser.find_element(By.ID, 'input_value')
    x = input.text
    y = calc(x)
        
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(y)
    
    button1 = browser.find_element(By.ID, 'solve')
    button1.click()
    
finally:
    time.sleep(20)
    browser.quit()