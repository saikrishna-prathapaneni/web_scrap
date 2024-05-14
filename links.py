import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_top_google_result(keyword):
    """Searches Google for the keyword and returns the first result's link.

    Args:
        keyword: The search term.

    Returns:
        str: The URL of the top result, or None if no result is found.
    """

    # Configure the webdriver (adjust if you use a different browser)
    driver = webdriver.Chrome()  

    try:
        driver.get("https://www.google.com")

        # Find the search box and enter the keyword
        search_bar = driver.find_element(By.NAME, "q")
        search_bar.send_keys(keyword)
        search_bar.send_keys(Keys.RETURN)

        # Wait for the results to load and get the top link
        try:
            top_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#search a[href]:has(h3)"))
            )
            link = top_result.get_attribute("href")
            return link
        except Exception:
            print(f"No results found for: {keyword}")
            return None

    finally:
        driver.quit()

def main():
    # Path to your CSV file
    csv_file_path = "data.csv" 

    # Open the CSV file and update it
    with open(csv_file_path, 'r', newline='') as infile, \
         open('updated_keywords.csv', 'w', newline='') as outfile: 

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Process each row (assuming keywords are in the first column)
        for row in reader:
            keyword = row[0]
            result_link = get_top_google_result(keyword)
            print(result_link, keyword)
            # Add the result link as a new column
            row.append(result_link) 
            writer.writerow(row)

if __name__ == "__main__":
    main()