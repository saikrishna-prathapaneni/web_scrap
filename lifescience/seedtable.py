import csv
from bs4 import BeautifulSoup

# Send a GET request to the URL and retrieve the HTML content
html_file = "file.html"

# Read the HTML file
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")


# Find all the list-card elements
list_cards = soup.find_all('div', class_='list-card')

# Initialize a list to store company information
companies = []

# Extract information for each company
for card in list_cards:
    # Extract the required information
    company_name = card.find('strong').text
    company_link = card.find('a', class_='list-btn')['href']
    description = card.find('p').text.strip()

    # Append the company information to the list
    companies.append({
        'Company Name': company_name,
        'Link': company_link,
        'Description': description
    })

# Save the extracted data as a CSV file
csv_file = 'seedtable.csv'
header = ['Company Name', 'Link', 'Description']

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=header)
    writer.writeheader()
    writer.writerows(companies)

print(f"Data saved successfully in {csv_file}.")
