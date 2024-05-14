import csv
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.hustlefund.vc/founders'
url = base_url
html_content = ""

while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    company_info_list = soup.find_all('div', class_='company-info')

    # Process the retrieved company information here...
    # ...

    # Check if there is a "SHOW MORE" button
    show_more_button = soup.find('div', class_='btn-text-show-more')
    if not show_more_button:
        break  # No more content to load

    # Extract the URL for the next page
    next_page_url = show_more_button.parent['href']
    url = base_url + next_page_url

    # Concatenate the HTML content
    html_content += response.text

# Process the complete HTML content here...
# ...

# Parse the complete HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the company-info elements
company_info_list = soup.find_all('div', class_='company-info')

# Create a CSV file and write the headers
csv_file = open('hustle.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Location', 'Sector', 'Startup Link'])

# Iterate over the company-info elements and extract the required information
for item in company_info_list:
    company_name = item.find('div', class_='company-title').text.strip()
    location = item.find('div', {'fs-cmsfilter-field': 'location'}).text.strip()
    sector = item.find('div', {'fs-cmsfilter-field': 'sectors'}).text.strip()
    startup_link = item.find('a')['href']

    # Write the data to the CSV file
    csv_writer.writerow([company_name, location, sector, startup_link])

# Close the CSV file
csv_file.close()
