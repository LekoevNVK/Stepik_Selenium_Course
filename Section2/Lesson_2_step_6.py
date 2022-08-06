import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def make_input(url):
    try:
        driver.get(url)
        x_value = int(driver.find_element(By.ID, "input_value").text)
        driver.find_element(By.ID, "answer").send_keys(calc(x_value))
        submit = driver.find_element(By.TAG_NAME, "button")
        driver.execute_script("return arguments[0].scrollIntoView(true);", submit)
        driver.find_element(By.ID, "robotCheckbox").click()
        driver.find_element(By.ID, "robotsRule").click()
        sleep(0.1)
        submit.click()
    finally:
        sleep(5)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


make_input("http://suninjuly.github.io/execute_script.html")
