import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
# Set up Selenium webdriver
chrome_driver_path = 'chromedriver.exe'  # Replace with the actual path to chromedriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Define URLs for the pages to scrape
urls = [
    "https://food-x.com/startups/?q=&idx=Company_production&p=0&fR%5Bvisible_to_public%5D%5B0%5D=true",
    "https://food-x.com/startups/?q=&idx=Company_production&p=1&fR%5Bvisible_to_public%5D%5B0%5D=true",
    "https://food-x.com/startups/?q=&idx=Company_production&p=2&fR%5Bvisible_to_public%5D%5B0%5D=true",
 

    #"https://food-x.com/startups/?q=&idx=Company_production&p=2&fR%5Bvisible_to_public%5D%5B0%5D=true&fR%5Bvisible_to_public%5D%5B1%5D=true"
]

# Prepare CSV file and header
csv_file = open('foodx.csv', 'w',encoding='utf-8',  newline='')
writer = csv.writer(csv_file)
writer.writerow(['Company Name', 'Company Link', 'Description'])

# Scrape data from each page
driver.get(urls[0])
while True:
    # Open the webpage
    

    # Find all the div elements containing company information
    company_divs = driver.find_elements(By.CLASS_NAME, 'ais-hits--item')
    print(len(company_divs))
    # Extract and write company information to CSV
    for div in company_divs:
        # Extract data from div elements
        company_name = div.find_element(By.CLASS_NAME, 'cardtitle').text
        company_link = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
        description = div.find_element(By.CLASS_NAME, 'cardtagline').text
        #location = div.find_element(By.CLASS_NAME, 'country').text

        # Write data to CSV
        writer.writerow([company_name, company_link, description])
    # b = driver.find_element(By.XPATH,"//*[@id='pagination-container']/div/ul/li[6]/a")
    # b.click()
    print("done")

    time.sleep(5)

# Close CSV file and browser
csv_file.close()
driver.quit()
