from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
# Initialize Selenium webdriver
driver = webdriver.Chrome()

# Load the webpage
driver.get('https://www.nfx.com/companies?showUnicorns=false')
wait = WebDriverWait(driver, 10)
#wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'vsc-initialized')))
# Find all the elements matching the specified CSS selector

time.sleep(10)
elements = driver.find_elements(By.CLASS_NAME, 'grid grid-cols-4 md:grid-cols-8 lg:grid-cols-12 gap-6 lg:gap-8 text-offBlue group border-b-[0.5px] border-offBlue/10')
filename = 'nfx.csv'

csv_file = open(filename, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Link', 'Description'])

print(len(elements))
#
# Create a list to store the extracted data
data = []

# Iterate over each element and extract the required information
for element in elements:
    # Click on the element to open the popup window
    
    locator = element.find_element(By.CLASS_NAME,'css-parwub')
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable(locator))
    button.click()

    # Wait for the popup window to load
    driver.implicitly_wait(5)  # Adjust the wait time if needed

    # Extract company name, link, description, and location
    try:
        company_name = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/div/div/div[2]/div/div/div/div/div[2]/p[1]').text
    #print(company_name)
    except:
        continue
    print(company_name)
    try:
    
        link = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/div/div/div[1]/div[2]/div/div/div/ul/a[2]').get_attribute('href')
    except:
        link = None
    try:

        description = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/div/div/div[2]/div/div/div/div/div[2]/p[2]').text
                                                    
    except:
        description= None

    try:
        location1 = driver.find_element(By.XPATH, '//*[@id="chakra-modal--body-:r3:"]/div/div[4]/div[1]/div/div[3]/div/div/ul/li[2]/span').text
    except:
        location1 =''
    
    try:

        location2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/div/div/div[4]/div[1]/div/div[3]/div/div/ul/li[1]/span').text
    except:
        try:
            location2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/div/div/div[4]/div[1]/div/div[3]/div/div/ul/li/span').text
        except:
            location2=''

    location = location2 +','+ location1 
    try:
        get_connected = driver.find_element(By.XPATH,'/html/body/div[4]/div[3]/div/section/div/div/div[1]/div[2]/div/div/div/ul/a[1]').get_attribute('href')
    except:
        get_connected = None
    # Add the extracted data to the list
    #data.append([company_name, link, description, location,get_connected])
    print([company_name, link, description, location,get_connected])
    csv_writer.writerow([company_name, link, description, location,get_connected])
    # Close the popup window
    close_button = driver.find_element(By.XPATH, '/html/body/div[4]/div[3]/div/section/header/button')
    close_button.click()

# Quit the webdriver
driver.quit()


# with open(filename, 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Company Name', 'Link', 'Description', 'Location','get connected'])
#     writer.writerows(data)

print(f'Data extracted and saved as {filename}')
