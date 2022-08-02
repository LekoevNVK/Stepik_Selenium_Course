import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

import complete_form as cf

browser = webdriver.Chrome()


def find_element_by_link():
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    browser.find_element(By.NAME, 'first_name').send_keys('Testontin')
    browser.find_element(By.NAME, 'last_name').send_keys('Testin')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Testoviy')
    browser.find_element(By.ID, 'country').send_keys('Testoviya Federation')
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()


find_element_by_link()
