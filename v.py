import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
# Path to the ChromeDriver executable
webdriver_path = "chromedriver.exe"

# URL of the page
csv_file = "alchemist.csv"

# Define the column index (starting from 0) that contains the links
column_index = 1

# Create an empty list to store the links
links = []

# Read the CSV file and extract the links from the specified column
with open(csv_file, 'r',encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        # Assuming the links are in the third column (index 2)
        link = row[column_index]
        links.append(str(link))




# Start the Selenium WebDriver
service = Service(webdriver_path)
driver = webdriver.Chrome(service=service)

# Load the page

websites =[]
for link in links[1:]:
    print(link)
    try:
        driver.get(link)
    except:
        continue
 
    try:
        website_element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.dsa-social-icon__text-url')))
    # Find the link element with class "dsa-social-icon__text-url"
        websites.append(website_element.get_attribute("href"))
    except:
        websites.append(None)
    
driver.quit()
# Define the path of the CSV file
csv_file = "vvv.csv"
with open(csv_file, mode='w',encoding='utf-8',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Link', 'Website'])
    for link, website in zip(links, websites):
        writer.writerow([link, website])

print("CSV file saved successfully!")

# Quit the WebDriver

