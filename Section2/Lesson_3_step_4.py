import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def complete_task(url):
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        alert = driver.switch_to.alert
        alert.accept()
        value_x = driver.find_element(By.ID, "input_value").text
        driver.find_element(By.ID, "answer").send_keys(calc(value_x))
        driver.find_element(By.CLASS_NAME, "btn").click()
    finally:
        sleep(4)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


complete_task("http://suninjuly.github.io/alert_accept.html")
