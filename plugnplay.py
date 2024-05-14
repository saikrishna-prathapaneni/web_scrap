import requests
from bs4 import BeautifulSoup
import csv
import re
# Send a GET request to the website

# Read the HTML file
html_file = 'file.html'
with open(html_file, "r", encoding="utf-8") as file:
    html_data = file.read()
soup = BeautifulSoup(html_data, "html.parser")
# Parse the HTML content


# Find all the div elements with the specified class


# Find all the list items with the specified class
list_items = soup.find_all('li')

print(len(list_items))
# Create a CSV file and write the header row
csv_file = open('plugnplay_unicorn.csv', 'a',encoding="utf-8", newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Company Name', 'Description', 'Link'])

# Iterate over each list item and extract the required information
for item in list_items:
    company_name = item['data-name']
    description = item.find(class_='cell pnp__startup-description').text.strip()
    try:
        link = item.find('a', class_='pnp__startup-website-link')['href']
    except:
        link =""
    
    # Write the data to the CSV file
    csv_writer.writerow([str(company_name), str(description), str(link)])

# Close the CSV file
csv_file.close()
