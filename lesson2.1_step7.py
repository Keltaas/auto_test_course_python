from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)

try:
    browser.get(url)
    check = browser.find_element(By.ID, "robotCheckbox")
    check.click()
    check1 = browser.find_element(By.ID, "robotsRule")
    check1.click()
    text = browser.find_element(By.TAG_NAME, "img").get_attribute("valuex")
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(calc(int(text)))
    time.sleep(1)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(15)
finally:
    browser.close()
    browser.quit()
