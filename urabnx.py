import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Selenium WebDriver (assuming you have installed the appropriate driver for your browser)
driver = webdriver.Chrome()

# Navigate to the URLs
urls = [
    'https://urban-x.com/companies?41db5cfc_page=0',
    'https://urban-x.com/companies?41db5cfc_page=1',
    'https://urban-x.com/companies?41db5cfc_page=2',
    'https://urban-x.com/companies?41db5cfc_page=3',
    'https://urban-x.com/companies?41db5cfc_page=4',
    'https://urban-x.com/companies?41db5cfc_page=5'
]

csv_file = open('urbanx.csv', 'w',encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Link', 'Description'])

for url in urls:
    driver.get(url)

    # Wait for the div elements to be present
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'w-dyn-item')))
    
    # Find all the div elements with the specified class name
    div_elements = driver.find_elements(By.CLASS_NAME, 'w-dyn-item')

    # Extract data from each div element
    for div_element in div_elements:
        try:
            # Extract company name
            company_name = div_element.find_element(By.CLASS_NAME, 'heading-style-h5').text

            # Extract link
            link = div_element.find_element(By.CSS_SELECTOR, 'a.companies-collection_card').get_attribute('href')

            # Extract description
            description = div_element.find_element(By.CLASS_NAME, 'text-size-regular').text
        except:
            company_name = ''
            link = ''
            description = ''

        # Write the data to the CSV file
        csv_writer.writerow([company_name, link, description])

# Close the CSV file
csv_file.close()

# Close the browser
driver.quit()
