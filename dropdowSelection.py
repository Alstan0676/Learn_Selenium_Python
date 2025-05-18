from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Firefox()
url = "https://the-internet.herokuapp.com/dropdown"

driver.get(url)
time.sleep(2)

dropDownElement = driver.find_element(By.ID, 'dropdown')
SelectOptions = Select(dropDownElement)
option_text = "Option 3"
found = False

for option in SelectOptions.options:
    if(option.text == option_text):
        print("Found option 2")
        option.click()
        found = True
        break

if not found:    
    print(f"couldn't find '{option_text}' in options")

