import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def complete_form(url):
    try:
        driver.get(url)
        driver.find_element(By.NAME, "firstname").send_keys("Test_firstname")
        driver.find_element(By.NAME, "lastname").send_keys("Test_lastname")
        driver.find_element(By.NAME, "email").send_keys("Test@test.test")
        current_dir_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir_path, "test.txt")
        driver.find_element(By.ID, "file").send_keys(file_path)
        driver.find_element(By.CLASS_NAME, "btn").click()
    finally:
        time.sleep(4)
        driver.quit()


complete_form("http://suninjuly.github.io/file_input.html")
