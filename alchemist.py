import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Set up Selenium webdriver
chrome_driver_path = 'path_to_chromedriver'  # Replace with the actual path to chromedriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Define URLs for the pages to scrape
urls = [
    "https://www.alchemistaccelerator.com/portfolio-2?pno=1&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=2&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=3&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=4&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=5&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=6&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=7&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=8&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=9&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=10&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=11&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=12&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=13&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=14&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=15&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=16&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=17&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=18&hsLang=en",
    "https://www.alchemistaccelerator.com/portfolio-2?pno=19&hsLang=en"
]

# Prepare CSV file and header
csv_file = open('alchemist.csv', 'w',encoding='utf-8',  newline='')
writer = csv.writer(csv_file)
writer.writerow(['Company Name', 'Company Link', 'Description', 'Location'])

# Scrape data from each page
for url in urls:
    # Open the webpage
    driver.get(url)

    # Find all the div elements containing company information
    company_divs = driver.find_elements(By.CLASS_NAME, 'investors-hubdb-items')

    # Extract and write company information to CSV
    for div in company_divs:
        # Extract data from div elements
        company_name = div.find_element(By.CLASS_NAME, 'company-name').text
        company_link = div.find_element(By.TAG_NAME, 'a').get_attribute('href')
        description = div.find_element(By.CLASS_NAME, 'description').text
        location = div.find_element(By.CLASS_NAME, 'country').text

        # Write data to CSV
        writer.writerow([company_name, company_link, description, location])

# Close CSV file and browser
csv_file.close()
driver.quit()
