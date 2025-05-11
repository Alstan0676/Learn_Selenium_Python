from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get("https://www.saucedemo.com/")


viewport_size = [(100,400), (1080, 400), (467, 700), (467, 567)]

try:
    for width, height in viewport_size:
        driver.set_window_size(width, height)
        time.sleep(4)

finally:
    driver.close()
