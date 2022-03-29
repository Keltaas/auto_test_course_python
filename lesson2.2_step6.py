from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os


url = "http://suninjuly.github.io/execute_script.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)

try:
    browser.get(url)
    x = browser.find_element(By.ID, "input_value").text
    print(x)
    ans = str(math.log(abs(12*math.sin(int(x)))))
    print(ans)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(ans)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    input3 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    input3.click()
    time.sleep(1)

    button.click()
    time.sleep(15)
finally:
    browser.close()
    browser.quit()
