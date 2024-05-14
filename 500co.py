import csv
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
# Set up the Selenium webdriver
driver = webdriver.Chrome()

# Open the webpage
url = "https://500.co/companies"
driver.get(url)

# Find the div element with class name "table-rows"
div_element = driver.find_element(By.CLASS_NAME,"table-rows")

# Prepare the data to be saved as a CSV
data = []

while True:
    # Find all the company elements within the div element
    company_elements = div_element.find_element(By.CLASS_NAME,"table-row")

    for company_element in company_elements:
        # Extract company name
        company_name = company_element.find_element(By.CLASS_NAME,"table-value.company-name").text.strip()
        # Extract subindustry
        subindustry = company_element.find_element(By.XPATH,".//div[@class='table-sub-heading' and contains(text(), 'Sub-Industry')]/following-sibling::div[@class='table-value']").text.strip()
        # Extract location
        location = company_element.find_element(By.XPATH,".//div[@class='table-sub-heading company-location']/following-sibling::div[@class='table-value']").text.strip()
        
        # Append the extracted data to the list
        data.append([company_name, subindustry, location])

    try:
        # Check if the "Next" button is present
        next_button = driver.find_element(By.XPATH,"//li[@class='next']")
        # Click on the "Next" button
        next_button.click()
        # Wait for the page to load
        driver.implicitly_wait(3)
        # Find the div element with class name "table-rows" on the new page
        div_element = driver.find_element(By.ClASS_NAME,"table-rows")
    except NoSuchElementException:
        # Break the loop if the "Next" button is not found
        break

# Save the data as a CSV file
csv_file = "company_data.csv"
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Company Name", "Sub-Industry", "Location"])  # Write header row
    writer.writerows(data)  # Write data rows

# Close the webdriver
driver.quit()
