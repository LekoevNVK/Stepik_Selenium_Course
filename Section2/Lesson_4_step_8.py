import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()


def complete_task(url):
    try:
        driver.get(url)
        WebDriverWait(driver, 12).until(ec.text_to_be_present_in_element((By.ID, "price"), "100"))
        driver.find_element(By.ID, "book").click()
        value_x = int(driver.find_element(By.ID, "input_value").text)
        driver.find_element(By.ID, "answer").send_keys(calc(value_x))
        driver.find_element(By.ID, "solve").click()
    finally:
        time.sleep(4)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


complete_task("http://suninjuly.github.io/explicit_wait2.html")
