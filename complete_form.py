from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()


def complete_form(link):
    browser.get(link)
    browser.find_element(By.NAME, 'first_name').send_keys('Testontin')
    browser.find_element(By.NAME, 'last_name').send_keys('Testin')
    browser.find_element(By.CLASS_NAME, 'city').send_keys('Testoviy')
    browser.find_element(By.ID, 'country').send_keys('Testoviya Federation')
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
