from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://opensource-demo.orangehrmlive.com/")

parent_window = driver.current_window_handle
print(parent_window)

time.sleep(2)
Click_Button = driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']")
Click_Button.click()

time.sleep(2)
child_windows = driver.window_handles
print (child_windows)

for child in child_windows:
    if child != parent_window:
        print(child)
        driver.switch_to.window(child)

        time.sleep(5)
        email_input = driver.find_element(By.XPATH, "//input[@id='Form_submitForm_EmailHomePage']")
        time.sleep(1)
        email_input.send_keys("Hello@gmail.com")
        time.sleep(10)

        driver.close()

driver.switch_to.window(parent_window)
driver.find_element(By.NAME, 'username').send_keys('AlstanAuto')








