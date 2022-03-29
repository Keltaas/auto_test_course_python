from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


url = "http://suninjuly.github.io/file_input.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)

try:
    current_dir = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(current_dir, 'test.txt')
    browser.get(url)
    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Ivanov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("Ivanov")
    file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
    file.send_keys(path)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)
    time.sleep(15)
finally:
    browser.close()
    browser.quit()
