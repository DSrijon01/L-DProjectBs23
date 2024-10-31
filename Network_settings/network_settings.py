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

driver.get("https://www.selenium.dev/documentation/") 

driver.set_network_conditions(
    offline = True,
    Latency = 50, 
    download_troughput = 500*1024,
    upload_throuhgput = 500*1024
    
)
driver.get_network_conditions()

driver.get("https://www.selenium.dev/documentation/")

driver.set_network_conditions(
    offline = False, 
    latency = 5000,
    download_troughput = 250*1024,
    upload_throuhgput = 500*1024
)

driver.get_network_conditions()

