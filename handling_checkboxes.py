from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10) 


driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
time.sleep(2)

driver.maximize_window()
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)

check_boxes = 0

for checkbox in checkboxes:
    if checkbox.is_selected():
        check_boxes += 1;

print(check_boxes)
