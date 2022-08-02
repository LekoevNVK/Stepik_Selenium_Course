import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.youtube.com')
searchbar = driver.find_element(By.XPATH, '//input[@id="search"]')
searchButton = driver.find_element(By.XPATH, '//*[@id="search-icon-legacy"]/yt-icon')
driver.implicitly_wait(4)
searchbar.send_keys('QA Test')
searchButton.click()

