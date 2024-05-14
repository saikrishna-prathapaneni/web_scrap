import requests
from bs4 import BeautifulSoup
import csv

filename = 'file.html'

with open(filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

div_elements = soup.find_all('div', class_='cell auto')

# Create a CSV file and write the header row
with open('zx.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Company Name', 'Link', 'Description', 'Location'])

    # Write data rows to the CSV file
    for div in div_elements:
        company_name = div.find('p', class_='b-portfolio-grid__item--content__title').text.strip()
        
        try:
            link = div.find('a')['href']
        except:
            link = None
        description = div.find('p', class_='b-portfolio-grid__item--content__description').text.strip()
        location = div.find('p', class_='b-portfolio-grid__item--content__location').text.strip()

        writer.writerow([company_name, link, description, location])

print("Data saved to company_data.csv")
