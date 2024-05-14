import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Set up Chrome driver
chrome_options = Options()

chrome_options.add_argument("window-size=1200x600")
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode
driver_path = "chromedriver"  # Path to your Chrome driver executable
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Navigate to the website
url = "https://deerfield.com/?q=portfolio%20companies&sort_field[posts]=sortable_title&sort_direction[posts]=asc&page=2&view=list&archive=companies"  # Replace with the actual URL of the website
driver.get(url)
driver.implicitly_wait(10)
# Find and click the button
# button = driver.find_element(By.CLASS_NAME, "st-result")  # Replace with the appropriate method to locate the button
#button.click()

# Wait for the side window to appear
count =1
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='st-pagination-container']/button[2]"))))
while True:

    
    driver.implicitly_wait(10)
    button = driver.find_element(By.XPATH,f"//*[@id='st-results-container']/button[{count}]")
    button.click()

    wait = WebDriverWait(driver, 10)  # Adjust the timeout as needed
    side_window = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "modal-container")))
    driver.implicitly_wait(5)
    # Extract data from the side window
    try:
        company_name = side_window.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div[2]/span/div/div[1]/div[2]/h2").text.strip()
        print(company_name)
    except:
        company_name=None
    try:
        company_description = side_window.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/span/div/div[2]/div[1]/p").text
    except:
        company_description =None
    
    try:
        company_website = side_window.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/div[1]/div[2]/div/div/div/div[2]/span/div/div[2]/div[2]/span/a").get_attribute("href")
    except:
        company_website= None
    print(company_description, company_name, company_website)
#modal-default-button
    # Close the side window
    #driver.implicitly_wait(5)
    driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div[1]/button"))))
    #close_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div[1]/button")))
    #close_button=wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div[1]/button")))
    #close_button = side_window.find_element(By.XPATH, "//*[@id='app']/div[2]/div/div[1]/div[2]/div/div/div/div[1]/button")
    #close_button.click()
    count+=1
    print(count)
    if count == 47:
        driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='st-pagination-container']/button[2]"))))
        count =1
       

# Save data to CSV
    csv_file = "dep4.csv"
    header = ["Company Name", "Description", "Website"]
    data = [str(company_name), str(company_description), str(company_website)]

    with open(csv_file, "a", newline="", encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(data)

# Quit the driver
driver.quit()
