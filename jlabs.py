import csv
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

# Read the CSV file containing URLs
url_file = 'jlabscompanies.csv'
df_urls = pd.read_csv(url_file)

# Create a list to store the extracted company links
company_links = []

# Start the WebDriver
driver = webdriver.Chrome() 

# Iterate through each URL
for url in df_urls['URL']:
  driver.get(url)
  # Load the URL
  try:
    cookie_btn = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    cookie_btn.click()
  except:
    pass
  #driver.get(url)
  # Wait for company website link
  website_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cf_company-content-header-grp1-companyurl > a")))
  
  # Wait for the website link to become visible
  #website_link = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.cf_company-content-header-grp1-companyurl > a")))
  
  # Extract the website URL
  website_url = website_link.get_attribute("href")
  
  # Add the website URL to the list
  company_links.append(website_url)

# Quit the WebDriver  
driver.quit()

# Write the extracted links to a CSV file
with open('jlabs_url.csv', 'w', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['Website'])
  writer.writerows([[url] for url in company_links])

print('Company links extracted and saved to company_links.csv')