from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.thegoldbugs.com/")

try:
    # Wait for the form to be present
    from_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'form')))
    
    # Fill in first name
    fname_element = from_element.find_element(By.NAME, 'fname')
    fname_element.send_keys('Jhon')

    # Fill in last name
    lname_element = from_element.find_element(By.NAME, 'lname')
    lname_element.send_keys('Doe')

    # Fill in email
    email_element = from_element.find_element(By.ID, 'email-yui_3_17_2_1_1664570076619_2728-field')
    email_element.send_keys('jhondoe@yahoo.com')

    # Fill in subject
    subject_element = from_element.find_element(By.ID, 'textarea-yui_3_17_2_1_1664570076619_2730-field')
    subject_element.send_keys('Daydreaming69')

    # Fill in message
    message_element = from_element.find_element(By.TAG_NAME, 'textarea')
    message_element.send_keys('Daydreaming69')

    # Select checkbox
    response_element = from_element.find_element(By.NAME, 'checkbox-b5b9cc19-24e5-4c8c-960a-055837723942-field')
    response_element.click()
    print("Checkbox selected:", response_element.is_selected())

    # Use JavaScript to click the radio button if it's obstructed
    radio_element = from_element.find_element(By.NAME, 'radio-56c0f90d-260f-4304-b624-4635972a6fa9-field')
    driver.execute_script("arguments[0].click();", radio_element)

    # Select dropdown
    select_element = from_element.find_element(By.ID, 'select-e1f50715-c8a7-48eb-bc99-2c245676068c-field')
    select = Select(select_element)
    select.select_by_value('Other')

    # Select survey radio button
    survey_radio_element = from_element.find_element(By.XPATH, "//input[@value='-2']")
    driver.execute_script("arguments[0].click();", survey_radio_element)

    # Submit the form 
    from_element.submit
except Exception as e:
    print("An error occurred:", e)
finally:
    # Close the driver after a brief pause
    driver.quit()
