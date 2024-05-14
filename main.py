import csv
import requests
from bs4 import BeautifulSoup

url = "https://briia.io/founders"

# Send a GET request to the URL and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")
container_div = soup.find('section')
# Find the container div that contains the company profiles
#container_div = soup.find("div", class_="container")
print(len(container_div))
# Find all the rows within the container div that represent each company
company_rows = container_div.find("div")
company_rows = company_rows.find_all("div", class_="row")
print(len(company_rows))
# Create a list to store the extracted data
data = []

# Iterate over the company rows and extract the link, description, and name
for row in company_rows:
    # Find the link within the row
    link = row.find("a")["href"]

    # Find the description within the row
    description = row.find("div", class_="teaser").text.strip()

    # Find the name of the company within the row
    name = row.find("img")["alt"]

    # Append the extracted data as a tuple to the data list
    data.append((link, description, name))

# Define the path for the CSV file
csv_file = "briia.csv"

# Write the extracted data to the CSV file
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Link", "Description", "Name"])  # Write the header row
    writer.writerows(data)

print("CSV file created successfully.")
