from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up the ChromeDriver service
driver_path = 'path_to_chromedriver'
service = Service(driver_path)

# Set up the Chrome options
options = Options()
# options.add_argument('--headless')  # Run Chrome in headless mode

# Create a new ChromeDriver instance
driver = webdriver.Chrome(service=service, options=options)

# Load the HTML content from the link
link = 'https://airtable.com/embed/shrJKNRdiCnuPp17E/tbl39gJXPmEeRCmK5/viwno0C8JAkV9gPoq/recCwZfeOKS6ipseY'  # Replace with the actual link
driver.get(link)

# Find the down arrow button
down_arrow = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hyperbaseContainer"]/div[16]/div/div/div/div/div[1]/div/div/div/div[1]/div[3]')))
# Store the extracted data
all_data = []

i=0
time.sleep(10)

while True:
    # Find the elements and extract the data
    try:
        company_name_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hyperbaseContainer"]/div[16]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div')))
        try:
            link_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hyperbaseContainer"]/div[16]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[5]/div[2]/div/div/div/a')))
        except:
            link_element= None
        location_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hyperbaseContainer"]/div[16]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[4]/div[2]/div/div/div')))
        statement_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="hyperbaseContainer"]/div[16]/div/div/div/div/div[2]/div/div[2]/div/div/div[1]/div[3]/div[2]/div/div/div')))

        company_name = company_name_element.text
        link = link_element.get_attribute('href')
        location = location_element.text
        statement = statement_element.text
    except:
        company_name = None
        link = None
        location = None
        statement = None

    # Append the data to the list
    all_data.append({
        'Company Name': company_name,
        'Link': link,
        'Location': location,
        'Statement': statement
    })
    #print(all_data)

    # Click the down arrow button
    try:
        down_arrow.click()
    except:
        print("done",company_name )
    
        time.sleep(1)
    i+=1
    if i==400:
        break
    # Check if we have reached the end of the list
    df = pd.DataFrame(all_data)

# Store the extracted data in a CSV file
    df.to_csv('startup health 2.csv', index=False)
    

# Close the WebDriver
driver.quit()

# Convert the list of dictionaries to a DataFrame
# df = pd.DataFrame(all_data)

# # Store the extracted data in a CSV file
# df.to_csv('company_data.csv', index=False)
