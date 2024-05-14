from bs4 import BeautifulSoup
import csv

filename = 'file.html'

with open(filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

companies = soup.find_all('div', class_='row align-items-top')

data = []
print(len(companies))

for company in companies:
    # Extract company name
    try:
        company_name = company.find('span', class_='pink').text.strip()
    except:
        company_name= None
    # Extract company link
    try:
        company_link = company.find('a')['href']
    except:
        company_link = None
    # Extract company description
    try:
        company_description = company.find('div', class_='bio').text.strip()
    except:
        company_description = None
    data.append([company_name, company_link, company_description])

# Write the extracted data to a CSV file
output_filename = 'ventureout.csv'

with open(output_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Link', 'Company Description'])
    writer.writerows(data)

print(f"Data written to {output_filename} successfully.")
