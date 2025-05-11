from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

def test_dinner_cruise_goa():
    driver = setup_driver()
    try:
        # Navigate to the website
        driver.get("https://dinnercruisegoa.com")
        
        # Wait for the page to load
        wait = WebDriverWait(driver, 10)
        
        # Test if the main page loads successfully
        print("Testing main page load...")
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("Main page loaded successfully!")
        
        # Add more test cases here
        # For example:
        # - Check if navigation menu is present
        # - Verify if booking form is accessible
        # - Test contact information
        
        time.sleep(2)  # Give time to see the results
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_dinner_cruise_goa()

