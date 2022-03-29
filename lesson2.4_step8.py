from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


url = "http://suninjuly.github.io/explicit_wait2.html"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.174 YaBrowser/22.1.5.810 Yowser/2.5 Safari/537.36")
options.add_argument("accept=text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9")
browser = webdriver.Chrome(executable_path=r"E:\python\selenium\driver\chromedriver", options=options)
browser.implicitly_wait(5)

try:
    browser.get(url)
    b = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    but = browser.find_element(By.ID, "book")
    but.click()
    x = browser.find_element(By.ID, "input_value").text
    ans = str(math.log(abs(12 * math.sin(int(x)))))
    input_ans = browser.find_element(By.ID, "answer")
    input_ans.send_keys(ans)
    button = browser.find_element(By.ID, "solve")
    button.click()
    time.sleep(15)
finally:
    browser.close()
    browser.quit()
