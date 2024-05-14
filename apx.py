import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def extract_data_and_save_to_csv(driver, element):
    # Find the pop-up element
    pop_up_element = element.find_element(By.CLASS_NAME, 'modal--portfolio-item')

    # Extract the company name
    company_name = pop_up_element.find_element(By.CLASS_NAME, 'font-display').text.strip()

    # Extract the company description
    company_description = pop_up_element.find_element(By.CSS_SELECTOR, '.w-full.h-3/5.bg-brand-dark-blue.text-off-white.py-16.px-8.overflow-scroll > div > div:last-child').text.strip()

    # Extract the company link
    company_link = pop_up_element.find_element(By.CSS_SELECTOR, '.social li:first-child a').get_attribute('href')

    # Save the data to a CSV file
    with open('companies.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([company_name, company_description, company_link])

# Set up the Selenium webdriver
driver = webdriver.Chrome()  # Or use the appropriate webdriver for your browser
driver.get('https://apx.vc/our-portfolio')  # Replace with the actual webpage URL

# Find all the elements and click on each one to open the pop-up
portfolio_items = driver.find_elements(By.XPATH, 'portfolio-item portfolio-api fade-in')
print(len(portfolio_items))
for item in portfolio_items:
    print(item)
    #button = driver.find_element_by_xpath("xpath")
    #driver.execute_script("arguments[0].click();", button)
    item.click()

    # Wait for the pop-up to appear and call the function to extract the data
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'modal--portfolio-item')))
    extract_data_and_save_to_csv(driver, item)

    # Close the pop-up
    close_button = driver.find_element(By.CSS_SELECTOR, '.close-modal')
    close_button.click()

# Close the browser window
driver.quit()
