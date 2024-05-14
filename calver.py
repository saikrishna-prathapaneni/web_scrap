import requests
from bs4 import BeautifulSoup
import csv

filename = 'file.html'

with open(filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

div_elements = soup.find_all('div', class_='border-box')

print(len(div_elements))
# Create a CSV file and write the header row
with open('company_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Name', 'Link', 'Description', 'Location', 'Email'])

    # Write data rows to the CSV file
    for div in div_elements:
        
        try:
            company_name = div.find('h3').text.strip()
        except AttributeError:
            company_name = None

        try:
            link = div.find('a', class_='sbu-outline-button')['href']
        except (AttributeError, TypeError):
            link = None

        try:
            description = div.find('span').text
            # description= description.find('span').text
            print(description)
        except AttributeError:
            description = None

        try:
            location = div.find('p', class_='sbu-outline-button--red').text.strip()
        except AttributeError:
            location = None

        try:
            email = div.find('a', href=lambda href: href and href.startswith('mailto:')).text.strip()
        except AttributeError:
            email = None

        writer.writerow([company_name, link, description, location, email])

print("Data saved to company_data.csv")
