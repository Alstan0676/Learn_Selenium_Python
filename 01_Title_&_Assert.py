from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://www.cursor.com/")
time.sleep(2)

driver.maximize_window()
title = driver.title
print(title)
time.sleep(2)

assert "Cursor - The AI Code Editor" in title             #will check is title equal to given title

#driver.find_element(by.xpath(/html[1]/body[1]/nav[1]/div[1]/div[1]/div[1]/a[1]/span[1]))
driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/div[1]/div[1]/a[1]/span[1]").click()
time.sleep(1)

email_input = driver.find_element(By.CSS_SELECTOR, "input[id='radix-:R1a5pjsvbjsq:']")
email_input.send_keys("admin@cruiscape.com")
time.sleep(1)

driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(3)

password_input = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[2]/div[2]/input[1]")
password_input.send_keys("CS@admin1")

driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']").click()



