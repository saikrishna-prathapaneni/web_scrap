import csv
import requests
from bs4 import BeautifulSoup

urls = [
    "https://www.zx-ventures.com/company/atom-group/",
    "https://www.zx-ventures.com/company/banqu/",
    "https://www.zx-ventures.com/company/beer-hawk/",
    "https://www.zx-ventures.com/company/biobrew/",
    "https://www.zx-ventures.com/company/black-crown/",
    "https://www.zx-ventures.com/company/catalant-2/",
    "https://www.zx-ventures.com/company/cutwater-spirits/",
    "https://www.zx-ventures.com/company/evergrain/",
    "https://www.zx-ventures.com/company/flying-fish/",
    "https://www.zx-ventures.com/company/ghost-energy/",
    "https://www.zx-ventures.com/company/ginette/",
    "https://www.zx-ventures.com/company/goose-island/",
    "https://www.zx-ventures.com/company/hocus-pocus/",
    "https://www.zx-ventures.com/company/hoegaarden/",
    "https://www.zx-ventures.com/company/interdrinks/",
    "https://www.zx-ventures.com/company/isla-beverage/",
    "https://www.zx-ventures.com/company/jamaica-rum-vibes/",
    "https://www.zx-ventures.com/company/kona-beverage/",
    "https://www.zx-ventures.com/company/leaf-logistics/",
    "https://www.zx-ventures.com/company/lohn-bier/",
    "https://www.zx-ventures.com/company/pensa-systems/",
    "https://www.zx-ventures.com/company/perfect-draft/",
    "https://www.zx-ventures.com/company/saveur-biere/",
    "https://www.zx-ventures.com/company/super-coffee/",
    "https://www.zx-ventures.com/company/winnin/",
    "https://www.zx-ventures.com/company/ze-delivery/"
]

csv_data = []

i=0
for url in urls:
    # Fetch the HTML content from the URL
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    divs = soup.find_all('div', class_='grid-x')


    for div in divs:
        # Find the first 'a' tag within the div
        link = div.find('a')

        if link:
            # Extract the company link and the element residing in the link
            company_link = link['href'].split(',')[-1]
            company_name = link.text.strip()

            # Append the data to the CSV list
            csv_data.append([company_link, company_name])
        else:
            # If no link is found, append None values
            csv_data.append([None, None])
# Save the data as a CSV file
with open('zx2.csv', 'w',encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
