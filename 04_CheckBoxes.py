from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://dinnercruisegoa.com/contact/")
driver.maximize_window()

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    # Scroll the element into view
    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    time.sleep(0.5)  # Small delay to ensure the element is fully in view
    checkbox.click()
