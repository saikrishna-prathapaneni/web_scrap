from bs4 import BeautifulSoup
import csv

# Load the HTML from file.html
with open('file.html', 'r',encoding='utf-8') as file:
    html = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')

# Find all <div> elements with class="card"
cards = soup.find_all('div', class_='card')

# Prepare the data to be written to CSV
data = []
for card in cards:
    link = card.find('a', class_='card__link')
    company_link = link['href'] if link else ''

    name = card.find('h2', class_='post-title').text.strip()
    description = card.find('p').text.strip()

    # Find the specific element <p><a href="http://dayoneresponse.com" target="_blank" rel="noopener">dayoneresponse.com</a></p>
    specific_element = card.find('p').find('a', href='http://dayoneresponse.com')
    specific_link = specific_element['href'] if specific_element else ''

    data.append([name, company_link, description, specific_link])

# Write the data to a CSV file
with open('companies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Link', 'Description', 'Specific Link'])
    writer.writerows(data)
