from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


url = "http://suninjuly.github.io/redirect_accept.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)
browser.implicitly_wait(5)

try:
    browser.get(url)
    but = browser.find_element(By.CSS_SELECTOR, "button.btn")
    but.click()
    browser.switch_to.window(browser.window_handles[1])
    x = browser.find_element(By.ID, "input_value").text
    ans = str(math.log(abs(12*math.sin(int(x)))))
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(ans)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(15)
finally:
    browser.close()
    browser.quit()
