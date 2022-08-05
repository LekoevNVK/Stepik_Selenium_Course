import math
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def complete_form(url):
    try:
        browser.get(url)
        value_x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
        browser.find_element(By.ID, "answer").send_keys(calc(value_x))
        browser.find_element(By.ID, "robotCheckbox").click()
        browser.find_element(By.ID, "robotsRule").click()
        browser.find_element(By.CLASS_NAME, "btn").click()
    finally:
        sleep(4)
        browser.quit()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


complete_form("http://suninjuly.github.io/get_attribute.html")
