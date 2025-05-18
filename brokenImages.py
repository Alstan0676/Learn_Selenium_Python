from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/broken_images"
driver.get(url)
driver.maximize_window()

Images = driver.find_elements(By.TAG_NAME, "img")
broken_images = []

for image in Images:
    src = image.get_attribute("src")

    if src:
        response = requests.get(src)

        if response.status_code != 200:
            #print(f"Broken Image: {src} (Status Code: '{response.status_code}')")
            ImageSrc = src
            broken_images.append(src)

for brokenImg in broken_images:
    print(f"broken-source: {brokenImg}")
driver.quit()
