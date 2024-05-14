import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
# Configure Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Run Chrome in headless mode

# Set path to your chromedriver
driver_path = "chromedriver.exe"

# Initialize Chrome webdriver
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)

# Open the webpage
# file= open("av_final.csv", "a", newline="", encoding="utf-8")
# writer = csv.writer(file)
# writer.writerow(["Company Name", "Company Link", "Description", "Geography"])


driver.get("https://live.collisionconf.com/cc23/attendees")
time.sleep(5)
#driver.implicit_wait(10)


# from bs4 import BeautifulSoup
# from selenium import webdriver
# import csv

# # Set up Selenium web driver
# driver = webdriver.Chrome()  # Change the path to the location of your web driver executable

# Load the HTML file
#driver.get('https://live.collisionconf.com/cc23/startups')  # Replace with the actual path to your HTML file



#link = "https://live.collisionconf.com"

# while True:
#     try: 
#          print("wait")
#     except:
#          break
time.sleep(30) 
#kma@stern.nyu.edu

while True:

# Find elements with the specified class name
    
    btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/header/nav/div/div[2]/button')))

    #btn = driver.find_element(By.XPATH,"/html/body/div[1]/main/div[2]/div/header/nav/div/div[2]/button")
    btn.click()
    checkboxes = driver.find_elements(By.CSS_SELECTOR, '.checkbox-control__label')

# Check the 3rd and 5th checkboxes
    checkboxes[2].click()  # Index 2 corresponds to the 3rd checkbox (0-based indexing)
    #checkboxes[4].click()  # Index 4 corresponds to the 5th checkbox (0-based indexing)

    
    #company_list = driver.find_element(By.CLASS_NAME, "attendee-item directory-item card -link")
    card_items = driver.find_element(By.CLASS_NAME('card__content'))

    # Iterate over the card items and extract the card heading and info
    output_list = []
    data = []
    for item in card_items:
        card_heading = item.find_element(By.CLASS_NAME('card__heading')).text
        info = item.find_element(By.CLASS_NAME('info')).text
        data.append([card_heading, info])

        # Define the CSV file path
        csv_file = 'output.csv'

        # Write the data to a CSV file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Card Heading', 'Info'])  # Write header row
            writer.writerows(data)  # Write data rows

    btn = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[2]/div/div/div/button[2]')))
    btn.click()
    # Extract the href attribute from each element
    # hrefs = [link+'/'+str(element.get_attribute('href')) for element in elements]
    # # Extract the required data using BeautifulSoup
    # soup = BeautifulSoup(driver.page_source, 'html.parser')

    # Find the elements and extract the data
   
    # company_name = soup.find('div', class_='logo-container').img['alt']
    # home_page = soup.find('a', title='homepage')['href']
    # description = soup.find('div', class_='profile-page__banner').text.strip()
    # ceo_name = soup.find('div', class_='profile-sidebar__sticky-box').text.strip()
    # ceo_linkedin = soup.find('a', title='LinkedIn')['href']
    #country = ''  # Fill in the logic to extract the country information

    # # Save the data to a CSV file
    # with open('output.csv', 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     writer.writerow(['Company Name', 'Home Page', 'Description', 'CEO Name', 'CEO LinkedIn', 'Country'])
    #     writer.writerow([company_name, home_page, description, ceo_name, ceo_linkedin, country])

# Close the web driver
driver.quit()
