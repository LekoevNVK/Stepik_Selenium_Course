import math
from selenium import webdriver
from selenium.webdriver.common.by import By

from complete_form import complete_form as cf

browser = webdriver.Chrome()


def find_element_by_link():
    browser.get('http://suninjuly.github.io/find_link_text')
    link = browser.find_element(By.LINK_TEXT, str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link.click()
    current_link = browser.current_url
    browser.quit()
    cf(current_link)


find_element_by_link()
