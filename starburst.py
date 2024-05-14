import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium webdriver
chrome_driver_path = 'chromedriver.exe'  # Replace with the actual path to chromedriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open the webpage
url = "https://starburst.aero/portfolio/"  # Replace with the actual URL
driver.get(url)

# Prepare CSV file and header
csv_file = open('starburst.csv', 'w',newline='')
writer = csv.writer(csv_file)
writer.writerow(['Company Name', 'Description', 'Location','Link'])

# Scrape data from each page

while True:
    # Find all the div elements containing company information
    wait = WebDriverWait(driver, 10)  # Adjust the timeout value as needed
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'col-12')))
    company_divs = driver.find_elements(By.CLASS_NAME, 'col-12')
    print(len(company_divs))
    # Extract and write company information to CSV
    time.sleep(2)
    i=1
    for div in company_divs:
        if i==13:
            break
        # Extract data from div elements
        company_name = div.find_element(By.XPATH, f'//*[@id="main"]/section[3]/div/div[1]/div[{i}]/div/a').text
                                                    
        print(company_name)
        try:
            description = div.find_element(By.XPATH, f'//*[@id="main"]/section[3]/div/div[1]/div[{i}]/div/div[2]/p').text
        except:
            description = None                                       
        try:                                   
            location1 = div.find_element(By.XPATH, f'//*[@id="main"]/section[3]/div/div[1]/div[{i}]/div/div[1]').text
        except:                                          
            location1 =""
        
        location= location1
        try:                                   
            link = div.find_element(By.XPATH, f'//*[@id="main"]/section[3]/div/div[1]/div[{i}]/div/a').get_attribute('href')
        except:
            link = None                               
        # Write data to CSV
        i+=1
        print([company_name, description, location, link])
        writer.writerow([company_name, description, location, link])

    # Check if there is a next button
    next_button = driver.find_element(By.CLASS_NAME, 'startups__navigation--next')
    i=1
    if 'startups__navigation--disabled' in next_button.get_attribute('class'):
        break
    
    # Click the next button
    next_button.click
