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

def getWebElement(self, locatorValue, locatorType):
    webElement = None
    try:
        locatorType = locatorType.lower()
        locatorByType = self.getLocatorType(locatorType)
        webElement = self.driver.find_element(locatorByType, locatorValue)
        self.log.info("WebElement found with locator value " + locatorValue + " using locatorType " + locatorByType)
    except:
        self.log.error("WebElement not found with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()
    return webElement

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()
## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()

## Click Event
def clickOnElement(self, locatorValue, locatorType):
    try:
        locatorType = locatorType.lower()
        webElement = self.waitForElement(locatorValue, locatorType)
        webElement.click()
        self.log.info("Clicked on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
    except:
        self.log.error("Unable to Click on WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        print_stack()