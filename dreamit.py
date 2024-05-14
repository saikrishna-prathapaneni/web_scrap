from bs4 import BeautifulSoup
import csv

# Open the HTML file
with open('file.html', 'r',encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all div elements with the specified class
div_elements = soup.find_all('div', class_='summary-item-record-type-image')

print(len(div_elements))
# Define the CSV file path
csv_file = 'dreamit.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Company Name', 'Company Link', 'Description', 'Location'])

    # Iterate over the div elements
    for div in div_elements:
        # Extract the company name
        company_name = div.find('a', class_='summary-thumbnail-container')['data-title']
        
        # Extract the company link
        company_link = div.find('a', class_='summary-thumbnail-container')['href']
        
        # Extract the description
        description = div.find('div', class_='summary-excerpt').text.strip()
        
        # Extract the location
        try:
            location = div.find('span', class_='summary-metadata-item--location').text.strip()
        except:
            location= None
        # Write the data to the CSV file
        writer.writerow([company_name, company_link, description, location])

print(f"Data has been extracted and saved to {csv_file}.")
