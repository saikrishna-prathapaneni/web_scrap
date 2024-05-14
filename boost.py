import csv
from bs4 import BeautifulSoup
import requests

# Fetch the HTML content from the URL
url = 'https://www.boost.vc/portfolio'
response = requests.get(url)
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the summary-item elements
summary_items = soup.find_all('div', class_='summary-item')

# Create a CSV file and write the headers
csv_file = open('boost.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Startup Link', 'Location', 'Description'])

# Iterate over the summary-items and extract the required information
for item in summary_items:
    
    company_name = item.find('a', class_='summary-title-link').text.strip()
    startup_link = item.find('a', class_='summary-title-link')['href']
    
    location = item.find('em').get_text(strip=True) if item.find('em') else ""
    description = item.find('div', class_='summary-excerpt').text.strip()

    # Write the data to the CSV file
    csv_writer.writerow([company_name, startup_link, location, description])

# Close the CSV file
csv_file.close()
