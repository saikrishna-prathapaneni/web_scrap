import csv
from bs4 import BeautifulSoup
import requests


# Open the HTML file and read its contents
with open('file.html', 'r') as file:
    html = file.read()

soup = BeautifulSoup(html,"html.parser")

startup_data=[]
# html= requests.get("https://www.collider.io/portfolio")
startup_divs = soup.find_all("div", {"class": "row sqs-row"})

print(len(startup_divs))

for div in startup_divs:
    #print(div)
    ele_lists= div.find('div', class_='col sqs-col-3 span-3')
    print(len(ele_lists))
    for ele in ele_lists:
        #company_name = ele.find('a', class_='sqs-block-image-link')['href']
        company_name = None
        #print(company_name)
        #find("div", {"id": "articlebody"})
        print(ele)
        link = ele.find('a', {"id": "yui_3_17_2_1_1687798002640_154"})['href']
        description = ele.find('noscript')['alt']
        startup_data.append([company_name, link, description])  

# Save the extracted data as a CSV file
with open('collider.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Company Name', 'Link', 'Description'])
    writer.writerows(startup_data)
