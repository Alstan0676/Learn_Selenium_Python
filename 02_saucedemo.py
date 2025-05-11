from selenium import webdriver
import time
from selenium.webdriver.common.by import By



webdriver = webdriver.Firefox()

webdriver.get("https://www.saucedemo.com/")

webdriver.maximize_window()

webdriver.find_element(By.ID, "user-name").send_keys("standard_user")
time.sleep(1)

webdriver.find_element(By.ID, "password").send_keys("secret_sauce")
time.sleep(1)

webdriver.find_element(By.ID, "login-button").click()
time.sleep(3)

element = webdriver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/span[1]")
print(f"Found element text: {element.text}")
assert "Products" in element.text 
print("Test Passed")

webdriver.quit()
