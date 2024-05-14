import csv
import requests
from bs4 import BeautifulSoup

# The HTML code you provided
with open('file.html', 'r',encoding='utf-8') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all the div elements with class="blog34_item"
company_divs = soup.find_all('div', class_='blog34_item')

# Initialize lists to store the extracted data
company_data = []

# Loop through each company div
for company_div in company_divs:
    # Extract the company name
    company_name = company_div.find('h5', class_='portfolio-name').text.strip()

    # Extract the company description
    company_description = company_div.find('p', class_='text-style-5lines').text.strip()

    # Extract the company link
    company_link = company_div.find('a', class_='blog34_title-link')['href']

    # Append the data as a tuple to the company_data list
    company_data.append((company_name, company_description, company_link))

# Define the CSV file path
csv_file_path = 'companies1.csv'

# Write the data to the CSV file
with open(csv_file_path, 'w', newline='',encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Company Name', 'Company Description', 'Company Link'])
    csv_writer.writerows(company_data)

print(f"Data has been saved to {csv_file_path}")
