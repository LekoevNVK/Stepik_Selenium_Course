from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def complete_form(url):
    try:
        browser.get(url)
        elements = browser.find_elements(By.XPATH, '//input[@type="text"]')
        submit_button = browser.find_element(By.CLASS_NAME, 'btn')
        for element in elements:
            element.send_keys('Тест')
        submit_button.click()
    finally:
        sleep(5)
        browser.quit()


complete_form('http://suninjuly.github.io/huge_form.html')