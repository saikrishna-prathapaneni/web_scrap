from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Define your search term
search_term = "Image Processing"

# URL for the arXiv CS search
search_url = "https://arxiv.org/search/cs"

# Set up the WebDriver (example with Chrome)
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": "/data",  # Change this path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})
driver = webdriver.Chrome(options=options)

# Open the search page
driver.get(search_url)

# Wait for the page to load and find the search input box
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "query")))
search_box = driver.find_element(By.ID, "query")
search_box.send_keys(search_term)

# Find the search button and click it
search_button = driver.find_element(By.CSS_SELECTOR, "button.button.is-link.is-medium")
search_button.click()

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "li.arxiv-result")))

# Find the first 'pdf' link in the results and click it
pdf_link = driver.find_element(By.XPATH, "//li[@class='arxiv-result']//a[contains(@href, '/pdf/')]")
pdf_link.click()

# Wait for the PDF page to load
# WebDriverWait(driver, 30).until(EC.number_of_windows_to_be(2))
# driver.switch_to.window(driver.window_handles[1])

# Get current URL (which should be the direct PDF link)
pdf_url = driver.current_url

print(pdf_url)

# Download the PDF file using requests
response = requests.get(pdf_url)
if response.status_code == 200:
    with open("latest_paper.pdf", "wb") as f:
        f.write(response.content)
    print("Paper downloaded successfully.")
else:
    print("Failed to download the paper.")

# Close the WebDriver
driver.quit()
