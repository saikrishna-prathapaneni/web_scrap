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
file= open("av_final.csv", "a", newline="", encoding="utf-8")
writer = csv.writer(file)
writer.writerow(["Company Name", "Company Link", "Description", "Geography"])


driver.get("https://www.av.vc/portfolio")


# Create a list to store the extracted data
data = []




while True:
    time.sleep(15)
    # Find the company list element
    company_list = driver.find_element(By.CLASS_NAME, "portfolio_list__KKdt9")
    companies = company_list.find_elements(By.TAG_NAME, "a")
    
    print(len(companies))
    # Loop through each company
    for company in companies:
        # Click on the company to open the pop-up
        time.sleep(1)
        print(company)
        company.click()
        # Wait for the pop-up to appear
        # element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f"//*[@id='body']/section/div[10]/div/div/div[3]/ul/li[1]/a")))
        # element.click()
        # Wait for the pop-up to load
        # element = driver.find_element(By.XPATH,f"/html/body/div/div/main/div/section/div[10]/div/div/div[3]/ul/li[{i}]/a")
        # element.click()
        # driver.implicitly_wait(3)

        # Find the pop-up element
        pop_up = driver.find_element(By.CLASS_NAME, "modal_modalwindow__fzOaS")

        # Extract company details
        try:
            company_name = pop_up.find_element(By.CLASS_NAME, "portfolio_companytitle__WwIFQ").text
        except:
            company_name = None
        
        try:
            company_link = pop_up.find_element(By.CLASS_NAME, "portfolio_companylink__mx_jj").find_element(By.TAG_NAME, "a").get_attribute("href")
        except:
            company_link = None
        try:

            description = pop_up.find_element(By.CLASS_NAME, "portfolio_description__Mfk0P").text
        except:
            description = None

        print(company_name,company_link, description)
        company_props = pop_up.find_element(By.CLASS_NAME, "portfolio_companyprops__8WN1G").text
        state =  re.search(r"Geography:\s*(.*)", company_props).group(1)

    
        # geography_element = company_props.find_element(By.XPATH, "//strong[text()='Geography:']")
        # geography = geography_element.find_element(By.XPATH, "./following-sibling::li").text.strip()
    #geography = pop_up.strip()
        print(company_name,company_link, description,state)
        # Add the extracted data to the list
        data.append([company_name, company_link, description,state])

        # Close the pop-up
        close_button = pop_up.find_element(By.CLASS_NAME, "modal_close__xV_T5")
        close_button.click()
       
    # Save the data as a CSV file

        writer.writerows(data)
    print("######################################################################################")
# Close the webdriver
driver.quit()
