from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests


driver = webdriver.Firefox()
url = "https://jqueryui.com/"
driver.get(url)
driver.maximize_window()
time.sleep(3)

All_links = driver.find_elements(By.TAG_NAME, 'a')
time.sleep(3)

for link in All_links:
    href = link.get_attribute('href')
    Response = requests.get(href)


    if Response.status_code > 400:
        print(f"Broken Link: {href} (Status_code: {Response.status_code})")

driver.quit()

