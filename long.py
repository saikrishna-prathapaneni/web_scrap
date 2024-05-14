from bs4 import BeautifulSoup
import csv

with open('file.html', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

data = [] 
ele= soup.find_all('div', class_='jet-listing-grid__item')

print(len(ele))
for div in ele:

    company_name = div.find('h2', class_='elementor-heading-title').text.strip()
    
    try:
        link = div.find('a', class_='jet-listing-dynamic-link__link')['href']
    except:
        link = None
    try:
        location = div.find('div', string='Location:').text.strip()
    except:
        location = None
    try:
        description = div.find('div', class_='elementor-widget-container').find('div', class_='elementor-widget-container').text.strip()
    except:
        description= None
    data.append([company_name, link, location, description])

with open('data.csv', 'w', newline='', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(['Company', 'Link', 'Location', 'Description'])
    for row in data:
        writer.writerow(row)