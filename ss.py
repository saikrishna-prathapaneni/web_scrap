import csv
from bs4 import BeautifulSoup

# HTML content

with open('file.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Create a BeautifulSoup object
# soup = BeautifulSoup(html, 'html.parser')

# Find the div elements with class "row"
rows = soup.find_all('div', class_='row')

# Create a list to store the extracted data
data = []

# Iterate over each row
for row in rows:
    # Extract the company name
    company_name = row.find('a')['href']

    # Extract the description
    description = row.find('div', class_='col-xs-10').text.strip()

    # Extract the link
    link = row.find('a')['href']

    # Append the extracted data to the list
    data.append([company_name, description, link])

# Save the data as a CSV file
with open('company_data.csv', 'w', newline='', encoding= 'utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Name', 'Description', 'Link'])
    writer.writerows(data)

print('Data saved successfully as company_data.csv')
