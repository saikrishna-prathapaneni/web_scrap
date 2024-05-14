

# Define the CSV file path

from bs4 import BeautifulSoup
import csv
import re
# Open the HTML file
with open('file.html', 'r',encoding='utf-8') as file:
    content = file.read()

# Parse the HTML content
soup = BeautifulSoup(content, 'html.parser')

# Find all article elements with the specified class
article_elements = soup.find_all('article', class_='companies-cell')

# Define the CSV file path
csv_file = 'entraprenuewsroundaccelerator.csv'

# Open the CSV file in write mode
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(['Company Name', 'Company Link', 'Description', 'Location', 'Founder Email'])

    # Iterate over the article elements
    for article in article_elements:
        try:
            # Extract the company name
            company_name = article.find('h2', class_='panel__headline').text.strip()
        except AttributeError:
            company_name = ''

        try:
            # Extract the company link
            company_link = article.find('a', href=True,string="Website")['href']
        except (AttributeError, TypeError):
            company_link = ''

        try:
            # Extract the description
            description = article.find('div', class_='panel__wysiwyg').text.strip()
        except AttributeError:
            description = ''

        try:
            # Extract the location
            location = article.find('span', class_='panel__category').text.strip()
        except AttributeError:
            location = ''

        try:
            # Extract the founder's email address
            founder_email = article.find_all('div', class_='panel__wysiwyg').find('p').text.strip()
            for text in founder_email:
                if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', text):
                    founder_email = text

        except AttributeError:
            founder_email = ''

        # Write the data to the CSV file
        writer.writerow([company_name, company_link, description, location, founder_email])

print(f"Data has been extracted and saved to {csv_file}.")
