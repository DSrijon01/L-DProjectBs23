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



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.selenium.dev/") 

search_elemenet = driver.find_element(By.CSS_SELECTOR, 'span.DocSearch-Button-Container')

search_elemenet.send_keys(Keys.CONTROL + 'k').send_keys('k').relase().perform()

#Search
input_element = driver.find_element(By.ID, 'docsearch-input')

#Find
input_element.send_keys('WebDriver')

#Action
action = ActionChains(driver=driver)

#Perform 
action.send_keys(Keys.ARROW_UP).perform()    

#Perform 
action.send_keys(Keys.ARROW_DOWN).perform() 

#Perform 
action.send_keys(Keys.ARROW_DOWN).perform() 

action.send_keys(Keys.ESCAPE).perform() 