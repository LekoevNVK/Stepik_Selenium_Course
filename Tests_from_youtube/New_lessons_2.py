import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from seleniumbase import BaseCase

browser = webdriver.Chrome()


def click_button():
    browser.get('https://www.google.com/')
    browser.find_element(By.XPATH, '//a[text()=" Как работает Google Поиск "]').click()


click_button()