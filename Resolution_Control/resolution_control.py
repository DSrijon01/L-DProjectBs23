from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Define mobile emulation
mobile_emulation = {'deviceName': 'iPad Mini'}

# Configure Chrome options for mobile emulation
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('mobileEmulation', mobile_emulation)

# Initialize the driver with mobile emulation options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

# Navigate to the URL
driver.get("https://www.selenium.dev/documentation/")

# Set an implicit wait time
driver.implicitly_wait(20)

# Additional actions can be added here
button_element = driver.find_element(By.CSS_SELECTOR, "button.navbar-toggler")
button_element.click()

# action chains 
action = ActionChains(driver=driver)

## Scroll Operation
driver.execute_script("window.scrollTo(0,800)")

# Close the driver after usage
time.sleep(5)  # Pause to view the emulated mobile site
driver.quit()
