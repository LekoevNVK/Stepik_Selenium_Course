import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def click_checkbox(url):
    try:
        browser.get(url)
        x_element = browser.find_element(By.ID, "input_value")
        browser.find_element(By.ID, "answer").send_keys(calc(x_element.text))
        browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']").click()
        browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
        browser.find_element(By.XPATH, "//button[@type='submit']").click()
    finally:
        sleep(4)
        browser.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


click_checkbox("https://suninjuly.github.io/math.html")
