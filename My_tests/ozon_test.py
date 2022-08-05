import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def find_all_elements():
    browser.get('https://www.ozon.ru')
    element_list = browser.find_elements(By.CLASS_NAME, 'cq9')
    assert len(element_list) == 13
    time.sleep(5)
    browser.quit()


find_all_elements()