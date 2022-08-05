from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def complete_form(url):
    try:
        browser.get(url)
        elements = browser.find_elements(By.XPATH, "//input[@type='text']")
        for element in elements:
            element.send_keys('Тест')
        browser.find_element(By.XPATH, "//button[contains(text(),'Submit')]").click()
    finally:
        sleep(5)
        browser.quit()


complete_form('http://suninjuly.github.io/find_xpath_form')
