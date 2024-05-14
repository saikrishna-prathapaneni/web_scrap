import re
import csv

filename = 'file.html'

with open(filename, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Define the regular expressions to extract company information
name_pattern = r'<span class="pink">(.*?)<\/span>'
link_pattern = r'<a href="(.*?)" target="_blank" rel="noopener">'
description_pattern = r'<div class="bio">(.*?)<\/div>'

# Extract company information using regular expressions
companies = re.findall(r'<div class="row carousel-item.*?>(.*?)<\/div>', html_content, re.DOTALL)

print(len(companies))
data = []

print(companies[0])
for company in companies:
    # Extract company name
    try:
        company_name = re.search(name_pattern, company, re.DOTALL).group(1).strip()
    except:
        company_name=None
    # Extract company link
    try:

        company_link = re.search(link_pattern, company, re.DOTALL).group(1)
    except:
        company_link = None
    # Extract company description
    try:
        company_description = re.search(description_pattern, company, re.DOTALL).group(1).strip()
    except:
        company_description= None
    data.append([company_name, company_link, company_description])

# Write the extracted data to a CSV file
output_filename = 'ven.csv'

with open(output_filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Company Link', 'Company Description'])
    writer.writerows(data)

print(f"Data written to {output_filename} successfully.")
