from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()


def complete_select(url):
    try:
        driver.get(url)
        num1 = int(driver.find_element(By.ID, "num1").text)
        num2 = int(driver.find_element(By.ID, "num2").text)
        select = Select(driver.find_element(By.TAG_NAME, "select"))
        select.select_by_value(str(num1 + num2))
        driver.find_element(By.CLASS_NAME, "btn").click()

    finally:
        sleep(5)
        driver.quit()


complete_select("http://suninjuly.github.io/selects1.html")
