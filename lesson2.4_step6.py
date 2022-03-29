from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


url = "http://suninjuly.github.io/cats.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)
browser.implicitly_wait(5)

try:
    browser.get(url)
    but = browser.find_element(By.ID, "button")
    but.click()
finally:
    browser.close()
    browser.quit()
