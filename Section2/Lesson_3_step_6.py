import math
from time import sleep
from selenium import webdriver as wd
from selenium.webdriver.common.by import By

driver = wd.Chrome()


def complete_task(url):
    try:
        driver.get(url)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        driver.switch_to.window(window_name=driver.window_handles[1])
        value_x = int(driver.find_element(By.ID, "input_value").text)
        driver.find_element(By.ID, "answer").send_keys(calc(value_x))
        driver.find_element(By.CLASS_NAME, "btn").click()
    finally:
        sleep(4)
        driver.quit()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


complete_task("http://suninjuly.github.io/redirect_accept.html")
