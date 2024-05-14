import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up Chrome options
chrome_options = Options()
#chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set up the Selenium Chrome driver
webdriver_service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Open the webpage #dp-dfg-items
driver.get('https://rockhealthcapital.com/portfolio/')  # Replace with the actual URL

# Find all elements with the specified type
elements = driver.find_elements(By.TAG_NAME, 'article')

print(len(elements))
# Create a CSV file to save the data
csv_file = open('rockhealth.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Company Description', 'Company Link'])

# Iterate over the elements and extract the data
for element in elements:
    # Click the element to trigger the popup
    # try:
    #     element.click()
    # except:
    #     continue
    time.sleep(3)
    # Wait for the popup element to appear
    #popup_element = driver.find_element(By.XPATH, '/html/body')
    #popup_element=wait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(driver.find_element_by_xpath("//iframe[@class='iframe_class']")))
    # Extract the data from the popup element class="dp-dfg-modal-content"
    iframe = driver.find_element(By.ID, 'dp-dfg-popup-modal-iframe')
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(iframe))
    
    # driver.switch_to.frame(iframe)
    try:
        company_name = driver.find_element(By.XPATH, '//*[@id="et-boc"]/div/div/div/div/div/div/div/div/h1').text
    except:
        company_name=None
    try:
        company_link = driver.find_element(By.XPATH, '//*[@id="et-boc"]/div/div/div/div/div/div/div/div/div/a').get_attribute('href')
    except:
        company_link = None
    try:

        company_description = driver.find_element(By.XPATH, '//*[@id="et-boc"]/div/div/div/div/div/div/div/div/p').text
    except:
        company_description = None
    print(company_name,company_description, company_link)
    time.sleep(2)
    driver.switch_to.default_content()
    close_button_locator = (By.CLASS_NAME, 'mfp-close')
    close_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(close_button_locator))
    close_button.click()
    # close_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/button')
    #ActionChains(driver).move_to_element(close_button).click().perform()
    
    # Write the data to the CSV file
    csv_writer.writerow([company_name, company_description, company_link])

# Close the CSV file
csv_file.close()

# Quit the Selenium driver
driver.quit()
