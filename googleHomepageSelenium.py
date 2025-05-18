
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36")

driver = webdriver.Firefox(options=options)
driver.maximize_window()

try:
    driver.get("https://m.google.com/")
    time.sleep(3)

    googleSearch = driver.find_element(By.CSS_SELECTOR, "#APjFqb")

    googleSearch.send_keys("QA Automation with Selenium" + Keys.RETURN)

    
    time.sleep(15)
    

finally: 
    driver.quit()

